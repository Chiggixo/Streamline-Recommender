import os

# Define folder structure
folders = [
    "product-recommender/data",
    "product-recommender/notebooks",
    "product-recommender/src"
]

files = {
    "product-recommender/main.py": "",
    "product-recommender/requirements.txt": "",
    "product-recommender/README.md": "",
    "product-recommender/src/preprocessing.py": "# Preprocessing logic here\n",
    "product-recommender/src/recommender.py": "# Recommendation logic here\n",
    "product-recommender/src/evaluation.py": "# Evaluation logic here\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("📁 Project structure created successfully!")
