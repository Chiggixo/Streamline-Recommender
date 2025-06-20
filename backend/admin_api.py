from fastapi import APIRouter, HTTPException
import json
import csv
import os

from backend.utils import load_metadata_dict

admin_router = APIRouter(prefix="/admin")

METADATA_PATH = os.path.abspath("data/product_metadata.json")
CSV_PATH = os.path.abspath("data/beauty_product_ratings.csv")

# ✅ Load product names for dropdown
@admin_router.get("/product-names/")
def get_metadata():
    metadata = load_metadata_dict()
    if isinstance(metadata, dict):
        return list(metadata.keys())
    return []

# ✅ Load full product metadata
@admin_router.get("/products/")
def get_all_products():
    try:
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        raise HTTPException(status_code=500, detail="Metadata loading failed")

# ✅ Add or update product
@admin_router.post("/add-product/")
def add_product(product: dict):
    try:
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            current_data = json.load(f)

        updated = False
        for item in current_data:
            if item["product_name"].lower() == product["product_name"].lower():
                item.update(product)
                updated = True
                break

        if not updated:
            current_data.append(product)

            # Get category and brand from input, fallback to "Misc" or "Unknown"
            category = product.get("category", "Misc")
            brand = product.get("brand", "Unknown")

            with open(CSV_PATH, "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "admin_test_user",
                    len(current_data),  # product_id
                    product["product_name"],
                    category,
                    brand,
                    5
                ])

        with open(METADATA_PATH, "w", encoding="utf-8") as f:
            json.dump(current_data, f, indent=2)

        return {"message": "✅ Product added/updated successfully"}
    except Exception as e:
        print("❌ Error in add_product:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

