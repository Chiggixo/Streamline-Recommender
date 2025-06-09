import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_processed_data(path="../data/beauty_product_ratings.csv"):
    return pd.read_csv(path)

def plot_top_categories(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='category', order=df['category'].value_counts().index, palette="Set2")
    plt.title("Top Product Categories")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

def plot_top_brands(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='brand', order=df['brand'].value_counts().index, palette="Set3")
    plt.title("Top Product Brands")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

def plot_rating_distribution(df):
    plt.figure(figsize=(5, 3))
    sns.histplot(df['rating'], bins=5, kde=False, color="skyblue")
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def eda_pipeline():
    print("📊 Starting EDA pipeline...")
    df = load_processed_data()

    print("🔍 Dataset Overview:")
    print(df.describe())
    print("\n🎯 Top 5 Products:\n", df['product_name'].value_counts().head())

    plot_top_categories(df)
    plot_top_brands(df)
    plot_rating_distribution(df)

if __name__ == "__main__":
    eda_pipeline()
