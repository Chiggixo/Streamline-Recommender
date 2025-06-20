import pandas as pd
import random

# ✅ Expanded product list with 10 products
products = [
    {"product_id": 1, "name": "Argan Hair Oil", "category": "Hair Care", "brand": "L'Oréal"},
    {"product_id": 2, "name": "Charcoal Face Wash", "category": "Skin Care", "brand": "WOW"},
    {"product_id": 3, "name": "Beard Trimmer X200", "category": "Tools", "brand": "Philips"},
    {"product_id": 4, "name": "Keratin Shampoo", "category": "Hair Care", "brand": "Tresemmé"},
    {"product_id": 5, "name": "Vitamin C Serum", "category": "Skin Care", "brand": "Mamaearth"},
    {"product_id": 6, "name": "Tea Tree Toner", "category": "Skin Care", "brand": "Biotique"},
    {"product_id": 7, "name": "Rosewater Mist", "category": "Skin Care", "brand": "Khadi"},
    {"product_id": 8, "name": "Hair Spa Cream", "category": "Hair Care", "brand": "L'Oréal"},
    {"product_id": 9, "name": "Aloe Vera Gel", "category": "Skin Care", "brand": "Patanjali"},
    {"product_id": 10, "name": "Nail Polish Remover Wipes", "category": "Tools", "brand": "Colorbar"}
]

# Generate users
users = [f"user_{i}" for i in range(1, 21)]

# Simulate interactions
data = []
for user in users:
    num_products = random.randint(4, 6)
    sampled = random.sample(products, num_products)
    for item in sampled:
        data.append({
            "user_id": user,
            "product_id": item["product_id"],
            "product_name": item["name"],
            "category": item["category"],
            "brand": item["brand"],
            "rating": random.randint(3, 5)
        })

# Save to CSV
df = pd.DataFrame(data)
csv_path = "data/beauty_product_ratings.csv"
df.to_csv(csv_path, index=False)
csv_path
