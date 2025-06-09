import React, { useState } from "react";
import "./App.css";

function App() {
  const [userId, setUserId] = useState("");
  const [productName, setProductName] = useState("");
  const [topN, setTopN] = useState(5);
  const [recommendations, setRecommendations] = useState([]);
  const [showResults, setShowResults] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setShowResults(false);

    const payload = {
      user_id: userId,
      product_name: productName,
      top_n: Number(topN),
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/recommend/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      setRecommendations(data.recommended_products);
      setTimeout(() => setShowResults(true), 300); // animation delay
    } catch (err) {
      alert("Error fetching recommendations");
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>Salon Product Recommender</h1>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>User ID</label>
          <input value={userId} onChange={(e) => setUserId(e.target.value)} required />
        </div>
        <div className="input-group">
          <label>Product Name</label>
          <input value={productName} onChange={(e) => setProductName(e.target.value)} required />
        </div>
        <div className="input-group">
          <label>Top N</label>
          <input type="number" value={topN} onChange={(e) => setTopN(e.target.value)} />
        </div>
        <button type="submit">Get Recommendations</button>
      </form>

      {showResults && (
        <div className="recommendation-list fade-in">
          <h2>Recommended Products</h2>
          <div className="card-container">
            {recommendations.map((item, idx) => (
              <div className="card" key={idx}>
                <strong>{item.product_name}</strong>
                {item.score !== null && <p>Score: {item.score}</p>}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
