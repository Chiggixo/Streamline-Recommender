import pandas as pd
from src.recommender import load_data


def get_top_popular_products(df, top_n=5):
    """
    Return top-N most frequently rated products.
    """
    popular = df['product_name'].value_counts().head(top_n)
    return popular.index.tolist()


def get_recommendation_for_new_user():
    """
    For cold-start users, recommend most popular products.
    """
    df = load_data()
    return get_top_popular_products(df)


def get_recommendation_for_new_item(product_name, sim_df, top_n=5):
    """
    Recommend similar items to a new/cold product using content-based similarity.
    """
    if product_name not in sim_df.columns:
        print(f"'{product_name}' not found in similarity matrix.")
        return []

    similar_items = sim_df[product_name].sort_values(ascending=False)
    return similar_items.iloc[1:top_n + 1].index.tolist()


# Run basic test
if __name__ == "__main__":
    df = load_data()
    print("Top Products for Cold-Start Users:", get_top_popular_products(df))
