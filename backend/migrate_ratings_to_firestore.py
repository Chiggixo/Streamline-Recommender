import csv
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.firebase_config import firestore_db


def migrate_real_ratings(csv_path="data/beauty_product_ratings.csv"):
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                unique_id = f"{row['user_id']}_{row['product_id']}"
                firestore_db.collection("ratings").document(unique_id).set(row)

        print("✅ Real ratings uploaded to Firestore.")
    except Exception as e:
        print("❌ Failed to upload ratings:", e)


if __name__ == "__main__":
    migrate_real_ratings()
