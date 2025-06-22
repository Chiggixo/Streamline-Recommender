import json
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.firebase_config import firestore_db


def migrate_metadata_to_firestore(json_path="data/product_metadata.json"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            products = json.load(f)

        if not isinstance(products, list):
            raise ValueError("Invalid JSON format: expected a list of products")

        count = 0
        for product in products:
            doc_ref = firestore_db.collection("products").document(product["product_name"])
            doc_ref.set(product)
            count += 1

        print(f"✅ Successfully migrated {count} products to Firestore.")
    except Exception as e:
        print(f"❌ Migration failed: {str(e)}")

if __name__ == "__main__":
    migrate_metadata_to_firestore()
