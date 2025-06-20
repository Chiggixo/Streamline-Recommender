import React, { useState } from "react";
import "./App.css";

function UpdateProductForm() {
  const [productName, setProductName] = useState("");
  const [updatedFields, setUpdatedFields] = useState({
    image_url: "",
    price: "",
    description: "",
  });
  const [message, setMessage] = useState("");

  const handleUpdate = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const response = await fetch(`http://127.0.0.1:8000/admin/products/${productName}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedFields),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(`✅ ${data.message}`);
      } else {
        setMessage(`❌ Error: ${data.detail}`);
      }
    } catch (err) {
      setMessage("❌ Request failed.");
      console.error(err);
    }
  };

  return (
    <div className="update-form">
      <h2>Update Product Metadata</h2>
      <form onSubmit={handleUpdate}>
        <input
          type="text"
          placeholder="Product Name"
          value={productName}
          onChange={(e) => setProductName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="New Image URL"
          value={updatedFields.image_url}
          onChange={(e) =>
            setUpdatedFields({ ...updatedFields, image_url: e.target.value })
          }
        />
        <input
          type="text"
          placeholder="New Price"
          value={updatedFields.price}
          onChange={(e) =>
            setUpdatedFields({ ...updatedFields, price: e.target.value })
          }
        />
        <textarea
          placeholder="New Description"
          value={updatedFields.description}
          onChange={(e) =>
            setUpdatedFields({ ...updatedFields, description: e.target.value })
          }
        />
        <button type="submit">Update Product</button>
      </form>
      {message && <p style={{ marginTop: "10px" }}>{message}</p>}
    </div>
  );
}

export default UpdateProductForm;
