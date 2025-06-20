from src.recommender import (
    load_data,
    create_user_item_matrix,
    compute_similarity_matrix,
    get_top_n_similar_products
)
import pandas as pd

def precision_at_k(recommended_items, relevant_items, k=5):
    """
    Precision@K: How many recommended items in top K are relevant.
    """
    recommended_at_k = recommended_items[:k]
    hits = len(set(recommended_at_k) & set(relevant_items))
    return hits / k

def recall_at_k(recommended_items, relevant_items, k=5):
    """
    Recall@K: How many relevant items were found in the top K recommendations.
    """
    recommended_at_k = recommended_items[:k]
    hits = len(set(recommended_at_k) & set(relevant_items))
    return hits / len(relevant_items) if relevant_items else 0.0

def mean_reciprocal_rank(recommended_items, relevant_items):
    """
    MRR: How soon the first relevant item appears in recommendations.
    """
    for idx, item in enumerate(recommended_items):
        if item in relevant_items:
            return 1 / (idx + 1)
    return 0.0

def evaluate_all_users(k=5):
    df = load_data()
    user_item_matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    precision_list = []
    recall_list = []
    mrr_list = []

    for user_id in user_item_matrix.index:
        user_ratings = user_item_matrix.loc[user_id]
        purchased_items = user_ratings[user_ratings > 0].index.tolist()

        if len(purchased_items) < 2:
            continue

        # Hold out one item, use others to simulate recommendation
        test_relevant = set(purchased_items[1:])  # Items to compare against
        score_series = pd.Series(0, index=similarity_df.columns)

        for item in purchased_items:
            if item in similarity_df.columns:
                score_series += similarity_df[item]

        # Remove already purchased items
        for seen_item in purchased_items:
            if seen_item in score_series:
                score_series[seen_item] = -1

        # Recommend top-N
        recommended_items = score_series.sort_values(ascending=False).head(k).index.tolist()

        # Evaluate
        precision_list.append(precision_at_k(recommended_items, test_relevant, k))
        recall_list.append(recall_at_k(recommended_items, test_relevant, k))
        mrr_list.append(mean_reciprocal_rank(recommended_items, test_relevant))

    # Print average scores
    print(f"\nAverage Precision@{k}: {sum(precision_list)/len(precision_list):.2f}")
    print(f"Average Recall@{k}: {sum(recall_list)/len(recall_list):.2f}")
    print(f"Average MRR: {sum(mrr_list)/len(mrr_list):.2f}")

# Run the test case + full evaluation
if __name__ == "__main__":
    # Sample check for testing
    relevant_items = ["Keratin Shampoo", "Beard Trimmer X200"]
    recommended_items = ["Vitamin C Serum", "Beard Trimmer X200", "Charcoal Face Wash", "Argan Hair Oil", "Keratin Shampoo"]

    print("Precision@5:", precision_at_k(recommended_items, relevant_items, k=5))
    print("Recall@5:", recall_at_k(recommended_items, relevant_items, k=5))
    print("MRR:", mean_reciprocal_rank(recommended_items, relevant_items))

    # Evaluate across all users
    evaluate_all_users(k=10)
