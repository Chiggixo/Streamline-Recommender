import os
import json

def load_metadata_dict():
    path = os.path.abspath("data/product_metadata.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {item["product_name"]: item for item in data}
    except:
        return {}
