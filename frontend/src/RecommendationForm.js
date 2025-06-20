import React, { useState, useEffect } from "react";

function RecommendationForm() {
  const [userId, setUserId] = useState("chiggi23");
  const [productName, setProductName] = useState("");
  const [topN, setTopN] = useState(5);
  const [recommendations, setRecommendations] = useState([]);
  const [productOptions, setProductOptions] = useState([]);

  useEffect(() => {
    // Load dropdown from local metadata
    fetch("/data/product_metadata.json")
      .then(res => res.json())
      .then(data => setProductOptions(data.map(p => p.product_name)))
      .catch(err => console.error("❌ Failed to load product names", err));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = { user_id: userId, product_name: productName, top_n: Number(topN) };

    try {
      const res = await fetch("http://127.0.0.1:8000/recommend/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      setRecommendations(data.recommended_products);
    } catch (err) {
      alert("Error fetching recommendations");
      console.error(err);
    }
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>User ID</label>
          <input value={userId} onChange={(e) => setUserId(e.target.value)} required />
        </div>
        <div className="input-group">
          <label>Product Name</label>
          <select value={productName} onChange={(e) => setProductName(e.target.value)} required>
            <option value="">-- Select a Product --</option>
            {productOptions.map((name, idx) => (
              <option key={idx} value={name}>{name}</option>
            ))}
          </select>
        </div>
        <div className="input-group">
          <label>Top N</label>
          <input type="number" value={topN} onChange={(e) => setTopN(e.target.value)} min="1" />
        </div>
        <button type="submit">Get Recommendations</button>
      </form>

      {recommendations.length > 0 && (
        <div className="card-container">
          {recommendations.map((item, idx) => (
            <div key={idx} className="card">
              <img src={item.image_url} alt={item.product_name} className="product-image" />
              <h3>{item.product_name}</h3>
              <p><strong>Score:</strong> {item.score ?? "N/A"}</p>
              <p>{item.description}</p>
              <p><strong>Price:</strong> {item.price}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default RecommendationForm;
