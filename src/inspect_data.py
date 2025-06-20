import pandas as pd

# Load the dataset
df = pd.read_csv("../data/beauty_product_ratings.csv")



# Basic exploration
print("✅ Dataset Loaded Successfully!\n")
print("📊 Shape of the dataset:", df.shape)
print("\n📌 First 5 rows:\n", df.head())
print("\n🔍 Data types:\n", df.dtypes)
print("\n❓ Missing values:\n", df.isnull().sum())
print("\n🔁 Unique categories:", df['category'].unique())
print("🧴 Unique products:", df['product_name'].nunique())
