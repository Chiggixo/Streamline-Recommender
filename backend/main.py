from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.recommender_logic import generate_recommendations
from backend.admin_api import admin_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Chirag - FastAPI backend is running..."}

class RecommendRequest(BaseModel):
    user_id: str
    product_name: str
    top_n: int = 10

@app.post("/recommend/")
def recommend(request: RecommendRequest):
    try:
        result = generate_recommendations(
            user_id=request.user_id,
            product_name=request.product_name,
            top_n=request.top_n
        )
        return {"recommended_products": result}
    except Exception as e:
        print("❌ Error in recommend endpoint:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

app.include_router(admin_router)
