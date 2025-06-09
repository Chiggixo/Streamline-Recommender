import pandas as pd
from src.recommender import (
    load_data,
    create_user_item_matrix,
    compute_similarity_matrix,
    get_top_n_similar_products,
    prepare_text_features,
    build_content_similarity_matrix
)
from src..fallback import (
    get_top_popular_products,
    get_recommendation_for_new_item
)

def generate_hybrid_recommendations(user_id, product_name, top_n=5):
    df = load_data()
    user_item_matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    if user_id not in user_item_matrix.index:
        print(f"New user detected: {user_id}")
        return get_top_popular_products(df, top_n)

    if product_name not in similarity_df.columns:
        print(f"New product detected: {product_name}")
        df_unique = prepare_text_features(df)
        sim_df = build_content_similarity_matrix(df_unique)
        return get_recommendation_for_new_item(product_name, sim_df, top_n)

    print(f"Returning collaborative recommendations for existing user/product.")
    return get_top_n_similar_products(product_name, similarity_df, n=top_n).index.tolist()

# Example usage
if __name__ == "__main__":
    print("Hybrid for cold user:", generate_hybrid_recommendations("user_999", "Beard Trimmer X200"))
    print("Hybrid for cold product:", generate_hybrid_recommendations("user_1", "New Product XYZ"))
    print("Hybrid for known user/item:", generate_hybrid_recommendations("user_1", "Argan Hair Oil"))
