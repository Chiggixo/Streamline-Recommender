import pandas as pd


def load_data(path="../data/beauty_product_ratings.csv"):
    """
    Load the CSV file and return a DataFrame.
    """
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Check and fill/handle missing values
    """
    print("🔍 Before cleaning:", df.shape)
    df = df.drop_duplicates()

    # Optional: Drop rows with missing values
    df = df.dropna()

    print("✅ After cleaning:", df.shape)
    return df


def encode_features(df):
    """
    Encode categorical features like category and brand using one-hot encoding.
    """
    df_encoded = pd.get_dummies(df, columns=["category", "brand"], drop_first=True)
    return df_encoded


def preprocess_pipeline():
    """
    Run the full preprocessing pipeline and return the final cleaned DataFrame.
    """
    print("🚀 Starting preprocessing pipeline...")
    df = load_data()
    df = clean_data(df)
    df_encoded = encode_features(df)

    print("🎯 Final columns:", df_encoded.columns.tolist())
    print("📦 Processed DataFrame shape:", df_encoded.shape)

    return df_encoded


# Run the pipeline if this script is executed
if __name__ == "__main__":
    df_final = preprocess_pipeline()
