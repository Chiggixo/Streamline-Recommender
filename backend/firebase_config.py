import firebase_admin
from firebase_admin import credentials, firestore
import os

# ✅ Load Firebase credentials
cred_path = os.path.join(os.path.dirname(__file__), "firebase_key.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# ✅ Connect to Firestore
firestore_db = firestore.client()
