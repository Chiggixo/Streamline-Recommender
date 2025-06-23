from fastapi import APIRouter, HTTPException
from backend.firebase_config import firestore_db
import csv
import os

admin_router = APIRouter(prefix="/admin")

CSV_PATH = os.path.abspath("data/beauty_product_ratings.csv")

# ✅ Get product names for dropdown
@admin_router.get("/product-names/")
def get_metadata_names():
    try:
        products_ref = firestore_db.collection("products")
        docs = products_ref.stream()
        names = [doc.to_dict().get("product_name", "") for doc in docs]
        return [name for name in names if name]
    except Exception as e:
        print("❌ Failed to load product names:", e)
        raise HTTPException(status_code=500, detail="Failed to load product names")

# ✅ Get all product metadata
@admin_router.get("/products/")
def get_all_products():
    try:
        products_ref = firestore_db.collection("products")
        docs = products_ref.stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print("❌ Error fetching from Firestore:", e)
        raise HTTPException(status_code=500, detail="Failed to load products")

# ✅ Add or update product
@admin_router.post("/add-product/")
def add_or_update_product(product: dict):
    try:
        product_name = product.get("product_name")
        if not product_name:
            raise HTTPException(status_code=400, detail="Missing product_name")

        doc_ref = firestore_db.collection("products").document(product_name)
        doc_ref.set(product, merge=True)

        # Write to CSV (append)
        category = product.get("category", "Misc")
        brand = product.get("brand", "Unknown")
        with open(CSV_PATH, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "admin_test_user",
                product_name,
                product_name,
                category,
                brand,
                5  # default rating
            ])

        return {"message": "✅ Product added/updated successfully!"}

    except Exception as e:
        print("❌ Error in add_or_update_product:", e)
        raise HTTPException(status_code=500, detail="Failed to add product")
