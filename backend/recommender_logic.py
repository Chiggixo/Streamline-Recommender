from backend.firebase_config import firestore_db
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_recommendations(user_id: str, product_name: str, top_n: int = 10):
    print(f"⚙️  Recommending for user: {user_id}, product: {product_name}, top_n: {top_n}")

    # ✅ Fetch product metadata from Firebase
    docs = firestore_db.collection("products").stream()
    metadata = [doc.to_dict() for doc in docs]

    df = pd.DataFrame(metadata)
    if df.empty:
        print("❌ No products found in Firebase.")
        return []

    # ✅ Text feature generation
    df["combined_text"] = df["product_name"] + " " + df["category"] + " " + df["brand"]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df["combined_text"])

    # ✅ Find target product
    try:
        target_idx = df[df["product_name"].str.lower() == product_name.lower()].index[0]
    except IndexError:
        print("🟡 Cold-start product detected.")
        return df.sample(n=top_n).to_dict(orient="records")

    # ✅ Compute similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[target_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1: top_n + 1]

    # ✅ Format results
    recommendations = []
    for idx, score in sim_scores:
        item = df.iloc[idx].to_dict()
        item["score"] = round(score, 3)
        recommendations.append(item)

    print("✅ Final Recommendations:", [r["product_name"] for r in recommendations])
    return recommendations
