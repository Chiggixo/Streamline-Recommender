// src/UpdateProduct.js
import React, { useState } from "react";
import "./App.css";

function UpdateProduct() {
  const [productName, setProductName] = useState("");
  const [updatedFields, setUpdatedFields] = useState({
    image_url: "",
    description: "",
    price: "",
  });
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Updating...");

    try {
      const response = await fetch(`http://127.0.0.1:8000/admin/products/${productName}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_name: productName, ...updatedFields }),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Update failed");

      setStatus("✅ Product updated successfully.");
    } catch (err) {
      console.error(err);
      setStatus("❌ Update failed.");
    }
  };

  return (
    <div className="update-product">
      <h2>Update Product</h2>
      <form className="form" onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Product Name (existing)</label>
          <input value={productName} onChange={(e) => setProductName(e.target.value)} required />
        </div>
        <div className="input-group">
          <label>New Image URL</label>
          <input value={updatedFields.image_url} onChange={(e) => setUpdatedFields({ ...updatedFields, image_url: e.target.value })} />
        </div>
        <div className="input-group">
          <label>New Description</label>
          <input value={updatedFields.description} onChange={(e) => setUpdatedFields({ ...updatedFields, description: e.target.value })} />
        </div>
        <div className="input-group">
          <label>New Price</label>
          <input value={updatedFields.price} onChange={(e) => setUpdatedFields({ ...updatedFields, price: e.target.value })} />
        </div>
        <button type="submit">Update Product</button>
        <p>{status}</p>
      </form>
    </div>
  );
}

export default UpdateProduct;
