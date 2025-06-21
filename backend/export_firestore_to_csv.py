import csv
from backend.firebase_config import firestore_db

def export_to_csv(csv_path="data/exported_products.csv"):
    docs = firestore_db.collection("products").stream()
    products = [doc.to_dict() for doc in docs]

    if not products:
        print("⚠️ No data found in Firebase.")
        return

    fieldnames = products[0].keys()

    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    print(f"✅ Exported {len(products)} products to {csv_path}")

# Run only when executing this file directly
if __name__ == "__main__":
    export_to_csv()
