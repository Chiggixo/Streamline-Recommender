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
from backend.utils import load_metadata_dict

def enrich_metadata(product_scores_dict):
    meta = load_metadata_dict()
    enriched = []
    for product, score in product_scores_dict.items():
        info = meta.get(product, {})
        enriched.append({
            "product_name": product,
            "score": round(score, 4) if score else None,
            "image_url": info.get("image_url", ""),
            "description": info.get("description", "No description available."),
            "price": info.get("price", "N/A")
        })
    return enriched

def generate_hybrid_recommendations(user_id, product_name, top_n=10):
    df = load_data()
    user_item_matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    # Handle Cold Start User
    if user_id not in user_item_matrix.index:
        print("🟡 Cold-start user detected.")
        fallback = get_top_popular_products(df, top_n)
        return enrich_metadata({p: None for p in fallback})

    # Handle Cold Start Product
    if product_name not in similarity_df.columns:
        print("🟡 Cold-start product detected.")
        df_unique = prepare_text_features(df)
        sim_df = build_content_similarity_matrix(df_unique)
        fallback = get_recommendation_for_new_item(product_name, sim_df, top_n)
        return enrich_metadata({p: None for p in fallback})
        print("🔍 Cold-start product fallback sim_df.index:", sim_df.index.tolist())

    # Normal Flow
    print("✅ Known user/product path.")
    top_items = get_top_n_similar_products(product_name, similarity_df, n=top_n)
    return enrich_metadata(top_items)
