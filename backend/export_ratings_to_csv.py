import csv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.firebase_config import firestore_db

def export_firestore_to_csv():
    docs = firestore_db.collection("products").stream()

    with open("data/beauty_product_ratings.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "product_id", "product_name", "category", "brand", "rating"])

        for i, doc in enumerate(docs):
            product = doc.to_dict()
            writer.writerow([
                "simulated_user",
                i + 1,
                product.get("product_name", ""),
                product.get("category", "Misc"),
                product.get("brand", "Unknown"),
                5  # Simulated default rating
            ])

    print("✅ Firestore data exported to beauty_product_ratings.csv")

if __name__ == "__main__":
    export_firestore_to_csv()
