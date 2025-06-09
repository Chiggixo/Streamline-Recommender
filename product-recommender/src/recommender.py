import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def load_data(path="data/beauty_product_ratings.csv"):

    """
    Load the preprocessed dataset.
    """
    return pd.read_csv(path)


def create_user_item_matrix(df):
    """
    Create a user-item matrix from the ratings.
    """
    user_item_matrix = df.pivot_table(index='user_id', columns='product_name', values='rating').fillna(0)
    return user_item_matrix


def compute_similarity_matrix(user_item_matrix):
    """
    Compute cosine similarity between items (products).
    """
    similarity = cosine_similarity(user_item_matrix.T)
    similarity_df = pd.DataFrame(similarity,
                                 index=user_item_matrix.columns,
                                 columns=user_item_matrix.columns)
    return similarity_df


def get_top_n_similar_products(product_name, similarity_df, n=5):
    """
    Get top N similar products for a given product.
    """
    if product_name not in similarity_df.columns:
        print(f"❌ Product '{product_name}' not found in the dataset.")
        return []

    similar_items = similarity_df[product_name].sort_values(ascending=False)
    top_n = similar_items.iloc[1:n + 1]  # Exclude the product itself
    return top_n


def run_recommender(product_name):
    """
    Main function to load data, compute similarity, and recommend similar products.
    """
    print("🚀 Running Collaborative Filtering Recommender...")
    df = load_data()
    user_item_matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity_matrix(user_item_matrix)

    print(f"\n🔍 Top 5 products similar to: '{product_name}'")
    top_similar = get_top_n_similar_products(product_name, similarity_df)
    print(top_similar)
    return top_similar


# Example usage:
if __name__ == "__main__":
    run_recommender("Argan Hair Oil")



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def prepare_text_features(df):
    """
    Create a deduplicated product feature dataset for content-based filtering.
    """
    df_unique = df.drop_duplicates(subset=['product_name']).copy()
    df_unique['text_features'] = df_unique['product_name'] + " " + df_unique['category'] + " " + df_unique['brand']
    df_unique.set_index('product_name', inplace=True)
    return df_unique



def build_content_similarity_matrix(df_unique):
    """
    Compute TF-IDF similarity between unique product text features.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df_unique['text_features'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    sim_df = pd.DataFrame(similarity_matrix,
                          index=df_unique.index,
                          columns=df_unique.index)
    return sim_df



def get_similar_products_content_based(product_name, sim_df, n=5):
    """
    Recommend top N similar products based on TF-IDF similarity.
    """
    if product_name not in sim_df.columns:
        print(f"Product '{product_name}' not found.")
        return []

    try:
        similarity_scores = sim_df.loc[:, product_name]
        if isinstance(similarity_scores, pd.DataFrame):
            # If we got a DataFrame instead of a Series, reduce it to Series
            similarity_scores = similarity_scores.iloc[:, 0]

        similar_items = similarity_scores.sort_values(ascending=False)
        return similar_items.iloc[1:n+1]
    except Exception as e:
        print("Error while computing content-based recommendations:", str(e))
        return []


    # Exclude the same product


def run_content_based_recommender(product_name):
    """
    Main function to run content-based filtering recommender.
    """
    print("🚀 Running Content-Based Recommender...")
    df = load_data()
    df = prepare_text_features(df)
    sim_df = build_content_similarity_matrix(df)

    print(f"\n🔍 Top 5 similar products to: '{product_name}' (based on features)")
    top_similar = get_similar_products_content_based(product_name, sim_df)
    print(top_similar)
    return top_similar


# Example run
if __name__ == "__main__":
    run_content_based_recommender("Argan Hair Oil")
