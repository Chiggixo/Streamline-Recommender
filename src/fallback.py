import pandas as pd
from src.recommender import load_data


# ✅ Get top popular products by average rating
def get_top_popular_products(df, top_n=10):
    top = df.groupby("product_name")["rating"].mean().sort_values(ascending=False).head(top_n)
    return list(top.index)



def get_recommendation_for_new_user():
    """
    For cold-start users, recommend most popular products.
    """
    df = load_data()
    return get_top_popular_products(df)


# ✅ Recommend for new product using content similarity
def get_recommendation_for_new_item(product_name, sim_df, top_n):
    if product_name not in sim_df.index:
        print(f"❌ {product_name} not in content sim index.")
        return []

    sim_scores = sim_df.loc[product_name].drop(product_name, errors="ignore")
    return sim_scores.sort_values(ascending=False).head(top_n).to_dict()


# Run basic test
if __name__ == "__main__":
    df = load_data()
    print("Top Products for Cold-Start Users:", get_top_popular_products(df))
