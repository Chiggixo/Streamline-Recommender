import os
import json
from backend.utils import load_metadata_dict
from src.hybrid import generate_hybrid_recommendations

def generate_recommendations(user_id: str, product_name: str, top_n: int = 10):
    print(f"⚙️  Recommending for user: {user_id}, product: {product_name}, top_n: {top_n}")
    metadata = load_metadata_dict()

    raw_recommendations = generate_hybrid_recommendations(
        user_id=user_id,
        product_name=product_name,
        top_n=top_n
    )

    results = []
    for rec in raw_recommendations:
        if isinstance(rec, dict):
            results.append(rec)
        else:
            meta = metadata.get(rec, {})
            results.append({
                "product_name": rec,
                "score": None,
                "image_url": meta.get("image_url", ""),
                "description": meta.get("description", "No description available."),
                "price": meta.get("price", "N/A")
            })
    print("✅ Final Recommendations:", results)
    return results
