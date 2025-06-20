import React, { useState, useEffect } from "react";
import axios from "axios";
import "./AdminPanel.css";
import Snackbar from "@mui/material/Snackbar";
import Alert from "@mui/material/Alert";

function AdminPanel() {
  const [products, setProducts] = useState([]);
  const [newProduct, setNewProduct] = useState({
    product_name: "",
    image_url: "",
    description: "",
    price: "",
    category: "",      // ✅ New field
    brand: "",         // ✅ New field
  });
  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success",
  });

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/admin/products/")
      .then((res) => setProducts(res.data || []))
      .catch((err) => console.error("Error fetching metadata:", err));
  }, []);

  const handleAddOrUpdate = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/admin/add-product/", newProduct);
      if (res.status === 200) {
        setSnackbar({
          open: true,
          message: "✅ Product added/updated successfully!",
          severity: "success",
        });
        setProducts((prev) => [...prev, newProduct]);
      }
    } catch (err) {
      console.error("Error adding product:", err);
      setSnackbar({
        open: true,
        message: "❌ Failed to add product",
        severity: "error",
      });
    }
  };

  const handleChange = (e) => {
    setNewProduct({ ...newProduct, [e.target.name]: e.target.value });
  };

  return (
    <div className="admin-panel">
      <h2>Admin Panel</h2>
      <div className="form-section">
        <input name="product_name" placeholder="Product Name" onChange={handleChange} />
        <input name="image_url" placeholder="Image URL" onChange={handleChange} />
        <input name="description" placeholder="Description" onChange={handleChange} />
        <input name="price" placeholder="Price (₹499)" onChange={handleChange} />
        <input name="category" placeholder="Category (e.g. Skin Care)" onChange={handleChange} />
        <input name="brand" placeholder="Brand (e.g. Mamaearth)" onChange={handleChange} />
        <button onClick={handleAddOrUpdate}>Add / Update Product</button>
      </div>

      <h3>All Products</h3>
      <div className="product-grid">
        {products.map((prod, idx) => (
          <div className="grid-card" key={idx}>
            <img src={prod.image_url} alt={prod.product_name} className="product-thumb" />
            <h4>{prod.product_name}</h4>
            <h5>{prod.description}</h5>
            <p>{prod.price}</p>
          </div>
        ))}
      </div>

      <Snackbar
        open={snackbar.open}
        autoHideDuration={3000}
        onClose={() => setSnackbar({ ...snackbar, open: false })}
      >
        <Alert
          onClose={() => setSnackbar({ ...snackbar, open: false })}
          severity={snackbar.severity}
        >
          {snackbar.message}
        </Alert>
      </Snackbar>
    </div>
  );
}

export default AdminPanel;
