import pandas as pd
from src.recommender import (
    load_data,
    create_user_item_matrix,
    compute_similarity_matrix,
    get_top_n_similar_products,
    prepare_text_features,
    build_content_similarity_matrix
)

from src.fallback import (
    get_top_popular_products,
    get_recommendation_for_new_item
)



def generate_hybrid_recommendations(user_id, product_name, top_n=5):
    df = load_data()
    user_item_matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    # Case 1: Cold-start user
    if user_id not in user_item_matrix.index:
        top_products = get_top_popular_products(df, top_n)
        return [{"product_name": p, "score": None} for p in top_products]

    # Case 2: Cold-start product
    if product_name not in similarity_df.columns:
        df = prepare_text_features(df)
        sim_df = build_content_similarity_matrix(df)
        fallback = get_recommendation_for_new_item(product_name, sim_df, top_n)
        return [{"product_name": p, "score": None} for p in fallback]

    # Known user and product
    top_items = get_top_n_similar_products(product_name, similarity_df, n=top_n)
    return [{"product_name": item, "score": round(score, 4)} for item, score in top_items.items()]

