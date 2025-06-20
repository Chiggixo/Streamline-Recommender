import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    return pd.read_csv("data/beauty_product_ratings.csv")

def create_user_item_matrix(df):
    return df.pivot_table(index="user_id", columns="product_name", values="rating", fill_value=0)

def compute_similarity_matrix(user_item_matrix):
    # Item-item similarity
    item_vectors = user_item_matrix.T
    sim_matrix = cosine_similarity(item_vectors)
    similarity_df = pd.DataFrame(sim_matrix, index=item_vectors.index, columns=item_vectors.index)
    return similarity_df

def get_top_n_similar_products(product_name, similarity_df, n=10):
    if product_name not in similarity_df.columns:
        return {}
    similar_scores = similarity_df[product_name].drop(labels=[product_name], errors="ignore")
    top_items = similar_scores.sort_values(ascending=False).head(n)
    return top_items.to_dict()

# For fallback content-based filtering
from sklearn.feature_extraction.text import TfidfVectorizer

def prepare_text_features(df):
    df_unique = df.drop_duplicates(subset="product_name").copy()  # ✅ copy to avoid SettingWithCopyWarning
    df_unique["combined_text"] = (
        df_unique["product_name"] + " " +
        df_unique["category"] + " " +
        df_unique["brand"]
    )
    return df_unique


def build_content_similarity_matrix(df_unique):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df_unique["combined_text"])
    sim_matrix = cosine_similarity(tfidf_matrix)
    sim_df = pd.DataFrame(sim_matrix, index=df_unique["product_name"], columns=df_unique["product_name"])
    return sim_df
