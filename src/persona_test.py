from hybrid import generate_hybrid_recommendations
import pandas as pd
from recommender import load_data

# Add persona test users
def inject_personas(df):
    persona_data = [
        {"user_id": "user_hair", "product_name": "Argan Hair Oil", "rating": 5},
        {"user_id": "user_hair", "product_name": "Keratin Shampoo", "rating": 4},

        {"user_id": "user_beard", "product_name": "Beard Trimmer X200", "rating": 5},

        {"user_id": "user_skin", "product_name": "Charcoal Face Wash", "rating": 5},
        {"user_id": "user_skin", "product_name": "Vitamin C Serum", "rating": 4},

        {"user_id": "user_glow", "product_name": "Rosewater Mist", "rating": 5},
        {"user_id": "user_glow", "product_name": "Aloe Vera Moisturizer", "rating": 4},

        {"user_id": "user_relax", "product_name": "Hair Spa Cream", "rating": 5},
        {"user_id": "user_relax", "product_name": "Tea Tree Toner", "rating": 4},

        {"user_id": "user_clean", "product_name": "Nail Polish Remover Wipes", "rating": 5},
    ]
    return pd.concat([df, pd.DataFrame(persona_data)], ignore_index=True)

def run_persona_tests():
    df = load_data()
    df = inject_personas(df)
    personas = {
        "user_hair": "Argan Hair Oil",
        "user_beard": "Beard Trimmer X200",
        "user_skin": "Charcoal Face Wash",
        "user_glow": "Rosewater Mist",
        "user_relax": "Hair Spa Cream",
        "user_clean": "Nail Polish Remover Wipes"
    }

    for user, product in personas.items():
        print(f"\nPersona: {user} liking '{product}'")
        recommendations = generate_hybrid_recommendations(user, product, top_n=5)
        for rec in recommendations:
            print(f"• {rec['product_name']} — Score: {rec['score']} — ₹{rec['price']} — {rec['description']}")

if __name__ == "__main__":
    run_persona_tests()
