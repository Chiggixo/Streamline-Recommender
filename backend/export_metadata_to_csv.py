import sys, os
import csv
from collections import OrderedDict

# 👇 Add parent path to sys.path so "backend.firebase_config" works
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.firebase_config import firestore_db


def export_to_csv(csv_path="data/exported_products.csv"):
    docs = firestore_db.collection("products").stream()
    products = [doc.to_dict() for doc in docs]

    if not products:
        print("⚠️ No data found in Firebase.")
        return

    # ✅ Collect all unique field names from all products
    all_fields = OrderedDict()
    for product in products:
        for key in product.keys():
            all_fields[key] = None
    fieldnames = list(all_fields.keys())

    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    print(f"✅ Exported {len(products)} products to {csv_path}")


if __name__ == "__main__":
    export_to_csv()
