import pandas as pd
import random

# Simulated product data
products = [
    {"product_id": 1, "name": "Argan Hair Oil", "category": "Hair Care", "brand": "L'Oréal"},
    {"product_id": 2, "name": "Charcoal Face Wash", "category": "Skin Care", "brand": "WOW"},
    {"product_id": 3, "name": "Beard Trimmer X200", "category": "Tools", "brand": "Philips"},
    {"product_id": 4, "name": "Keratin Shampoo", "category": "Hair Care", "brand": "Tresemmé"},
    {"product_id": 5, "name": "Vitamin C Serum", "category": "Skin Care", "brand": "Mamaearth"}
]

# Create fake user IDs
users = [f"user_{i}" for i in range(1, 21)]

# Simulate purchases
data = []

for user in users:
    num_products = random.randint(2, 4)
    purchased = random.sample(products, num_products)
    for item in purchased:
        data.append({
            "user_id": user,
            "product_id": item["product_id"],
            "product_name": item["name"],
            "category": item["category"],
            "brand": item["brand"],
            "rating": random.randint(3, 5)
        })

# Create a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("data/beauty_product_ratings.csv", index=False)

print("✅ Dataset saved to data/beauty_product_ratings.csv")
