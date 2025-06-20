import React, { useState } from "react";

function AdminPanel() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [authenticated, setAuthenticated] = useState(false);
  const [formData, setFormData] = useState({
    product_name: "",
    image_url: "",
    description: "",
    price: "",
  });

  const handleLogin = () => {
    if (username === "admin" && password === "admin123") {
      setAuthenticated(true);
    } else {
      alert("Invalid credentials");
    }
  };

  const handleInput = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleAddProduct = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/admin/products/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (res.status === 200) {
        alert("✅ Product added successfully");
        setFormData({ product_name: "", image_url: "", description: "", price: "" });
      } else {
        const data = await res.json();
        alert("❌ " + data.detail);
      }
    } catch (err) {
      alert("❌ Error adding product");
      console.error(err);
    }
  };

  return (
    <div className="admin-panel">
      {!authenticated ? (
        <>
          <h2>Admin Login</h2>
          <div className="input-group">
            <label>Username</label>
            <input value={username} onChange={(e) => setUsername(e.target.value)} />
          </div>
          <div className="input-group">
            <label>Password</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          <button onClick={handleLogin}>Login</button>
        </>
      ) : (
        <>
          <h2>Add New Product</h2>
          <div className="input-group">
            <label>Product Name</label>
            <input name="product_name" value={formData.product_name} onChange={handleInput} />
          </div>
          <div className="input-group">
            <label>Image URL</label>
            <input name="image_url" value={formData.image_url} onChange={handleInput} />
          </div>
          <div className="input-group">
            <label>Description</label>
            <input name="description" value={formData.description} onChange={handleInput} />
          </div>
          <div className="input-group">
            <label>Price</label>
            <input name="price" value={formData.price} onChange={handleInput} />
          </div>
          <button onClick={handleAddProduct}>Add Product</button>
        </>
      )}
    </div>
  );
}

export default AdminPanel;
