from fastapi import FastAPI
from pydantic import BaseModel
from backend.recommender_logic import generate_hybrid_recommendations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#  CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendRequest(BaseModel):
    user_id: str
    product_name: str
    top_n: int = 5

@app.post("/recommend/")
def recommend(request: RecommendRequest):
    print("Incoming request data:", request.dict())
    result = generate_hybrid_recommendations(
        request.user_id,
        request.product_name,
        request.top_n
    )
    print("Recommendations:", result)
    return {"recommended_products": result}


