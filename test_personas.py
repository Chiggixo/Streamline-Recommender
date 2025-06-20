from backend.recommender_logic import generate_hybrid_recommendations
import json, os

# Load metadata manually for enrichment
def load_metadata_dict():
    path = os.path.join(os.path.dirname(__file__), "data/product_metadata.json")
    with open(path, "r", encoding="utf-8") as f:
        return {entry["product_name"]: entry for entry in json.load(f)}

meta = load_metadata_dict()

# Simulated personas
test_cases = [
    {"user_id": "user_hair", "product_name": "Keratin Shampoo", "top_n": 5},
    {"user_id": "user_skin", "product_name": "Charcoal Face Wash", "top_n": 5},
    {"user_id": "user_beard", "product_name": "Beard Trimmer X200", "top_n": 5}
]

# Run each test case
for case in test_cases:
    print(f"\n>>> Persona: {case['user_id']} liking '{case['product_name']}'")
    results = generate_hybrid_recommendations(case['user_id'], case['product_name'], case['top_n'])

    for item in results:
        product = item["product_name"]
        enriched = meta.get(product, {})
        print(f"• {product} — Score: {item.get('score')} — ₹{enriched.get('price')} — {enriched.get('description')}")
