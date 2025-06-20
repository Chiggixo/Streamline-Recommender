import React, { useState, useEffect } from "react";
import axios from "axios";
import "./RecommendationForm.css";

function RecommendationForm() {
  const [userId, setUserId] = useState("");
  const [productName, setProductName] = useState("");
  const [topN, setTopN] = useState(5);
  const [productList, setProductList] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [showResults, setShowResults] = useState(false);

  // ✅ Fetch product list from backend
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/admin/product-names/")
      .then((res) => {
        console.log("Product list fetched:", res.data);  // ✅ debug line
        setProductList(res.data || []);
      })
      .catch((err) => {
        console.error("❌ Failed to fetch product list:", err);
      });
  }, []);

  // ✅ Submit recommendation request
  const handleSubmit = async (e) => {
    e.preventDefault();
    setShowResults(false);
    try {
      const response = await axios.post("http://127.0.0.1:8000/recommend/", {
        user_id: userId,
        product_name: productName,
        top_n: Number(topN),
      });
      setRecommendations(response.data.recommended_products || []);
      setTimeout(() => setShowResults(true), 300);
    } catch (error) {
      console.error("❌ Recommendation fetch failed:", error);
      alert("Failed to get recommendations. Please try again.");
    }
  };

  return (
    <div className="recommendation-form">
      <h2>Find Product Recommendations</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>User ID</label>
          <input
            type="text"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            placeholder="e.g. chirag23 or user_1"
            required
          />
        </div>

        <div className="input-group">
          <label>Product Name</label>
          <input
            list="product-names"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
            placeholder="Search or select"
            required
          />
          <datalist id="product-names">
            {productList.map((name, idx) => (
              <option key={idx} value={name} />
            ))}
          </datalist>
        </div>

        <div className="input-group">
          <label>
            Top N Recommendations{" "}
            {productList.length > 0 && `(max ${productList.length})`}
          </label>
          <input
            type="number"
            min={1}
            max={productList.length > 0 ? productList.length : 10}  // fallback to 10
            value={topN}
            onChange={(e) => setTopN(Number(e.target.value))}
            required
          />
        </div>

        <button type="submit" disabled={!userId || !productName}>
          Get Recommendations
        </button>
      </form>

      {showResults && recommendations.length > 0 && (
        <div className="results-container">
          <h3>Recommended Products</h3>
          <div className="card-container">
            {recommendations.map((product, idx) => (
              <div className="card" key={idx}>
                <img
                  src={product.image_url}
                  alt={product.product_name}
                  className="product-image"
                />
                <h4>{product.product_name}</h4>
                <p>
                  <strong>Score:</strong>{" "}
                  {product.score !== undefined ? product.score : "N/A"}
                </p>
                <p>{product.description}</p>
                <p>
                  <strong>Price:</strong> {product.price}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default RecommendationForm;
