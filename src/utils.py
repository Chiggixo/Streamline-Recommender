import os, json

def load_metadata_dict():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/product_metadata.json"))
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {entry["product_name"]: entry for entry in json.load(f)}
    except FileNotFoundError:
        return {}
