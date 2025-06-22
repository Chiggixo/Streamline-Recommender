import firebase_admin
from firebase_admin import credentials, firestore
import os

# ✅ Detect local vs Render (secret files)
# Local path fallback: backend/firebase_key.json
local_path = os.path.join(os.path.dirname(__file__), "firebase_key.json")
render_path = "/etc/secrets/firebase_key.json"

# Use the Render secret path if it exists
cred_path = render_path if os.path.exists(render_path) else local_path

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

firestore_db = firestore.client()
