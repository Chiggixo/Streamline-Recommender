import pandas as pd
from src.recommender import (
    create_user_item_matrix,
    compute_similarity_matrix,
    get_top_n_similar_products
)
from hybrid import generate_hybrid_recommendations
from src.recommender import load_data

# Step 1: Extend the dataset with fake users (personas)
def inject_personas(df):
    persona_data = [
        {"user_id": "user_hair", "product_name": "Argan Hair Oil", "rating": 5},
        {"user_id": "user_hair", "product_name": "Keratin Shampoo", "rating": 4},
        {"user_id": "user_beard", "product_name": "Beard Trimmer X200", "rating": 5},
        {"user_id": "user_skin", "product_name": "Charcoal Face Wash", "rating": 5},
        {"user_id": "user_skin", "product_name": "Vitamin C Serum", "rating": 4}
    ]
    df_persona = pd.DataFrame(persona_data)
    return pd.concat([df, df_persona], ignore_index=True)

# Step 2: Run recommendations for each persona
def run_persona_tests():
    df = load_data()
    df_extended = inject_personas(df)
    user_item_matrix = create_user_item_matrix(df_extended)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    personas = ["user_hair", "user_beard", "user_skin"]
    seed_products = {
        "user_hair": "Argan Hair Oil",
        "user_beard": "Beard Trimmer X200",
        "user_skin": "Charcoal Face Wash"
    }

    print("\n--- Persona-Based Testing (Simulated as Real Users) ---\n")
    for user in personas:
        print(f"Persona: {user}")
        base_product = seed_products[user]
        recs = get_top_n_similar_products(base_product, similarity_df, n=5)
        print("Recommendations:", recs.index.tolist())
        print()

if __name__ == "__main__":
    run_persona_tests()
