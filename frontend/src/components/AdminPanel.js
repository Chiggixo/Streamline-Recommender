from fastapi import APIRouter, HTTPException
from backend.firebase_config import firestore_db
from pydantic import BaseModel

admin_router = APIRouter(prefix="/admin")


# ✅ Define Product Schema
class Product(BaseModel):
    product_name: str
    image_url: str
    description: str
    price: str
    category: str
    brand: str


# ✅ Add or update product in Firestore
@admin_router.post("/add-product/")
def add_product(product: Product):
    try:
        doc_ref = firestore_db.collection("products").document(product.product_name)
        doc_ref.set(product.dict())  # set() creates or updates
        return {"message": "✅ Product added/updated successfully"}
    except Exception as e:
        print("❌ Firebase error:", str(e))
        raise HTTPException(status_code=500, detail="Failed to add product")


# ✅ Get product names for dropdown
@admin_router.get("/product-names/")
def get_product_names():
    try:
        docs = firestore_db.collection("products").stream()
        return [doc.id for doc in docs]
    except Exception as e:
        print("❌ Firebase fetch error:", str(e))
        raise HTTPException(status_code=500, detail="Failed to fetch product names")


# ✅ Get all product metadata
@admin_router.get("/products/")
def get_all_products():
    try:
        docs = firestore_db.collection("products").stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print("❌ Firebase read error:", str(e))
        raise HTTPException(status_code=500, detail="Failed to load products")
