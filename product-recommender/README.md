# Product Recommendation System for Salon Professionals

**Internship Project | Streamline Beauty India Pvt. Ltd.**  
**Intern:** Chirag  
**Domain:** Machine Learning & Full Stack Integration  
**Duration:** 45 Days

---

## 📌 Project Overview

A hybrid recommendation system that suggests salon products based on user-product interaction data using collaborative and content-based filtering. Designed to handle cold-start scenarios and simulate real-world user personas.

---

## 🚀 Features

- Collaborative Filtering (User-Item Matrix)
- Content-Based Filtering (TF-IDF Features)
- Cold Start Handling for new users/items
- Hybrid Logic Integration
- Persona-Based Testing
- Precision, Recall, MRR Evaluation
- React Frontend + FastAPI Backend
- Modern UI with animation
- Live API and Demo-Ready Frontend

---

## 🗂 Project Structure
Streamline-Recommender/
├── backend/
│   ├── main.py
│   ├── recommender_logic.py
│   └── fallback.py
├── src/
│   ├── recommender.py
│   ├── content_recommender.py
│   └── evaluation.py
├── data/
│   └── beauty_product_ratings.csv
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
├── screenshots/
│   ├── swagger.png
│   ├── react_output.png
│   ├── terminal_hybrid.png
│   └── persona_test.png
├── docs/
│   ├── Week1.pdf
│   └── Week2.pdf
├── README.md
└── requirements.txt

## 📥 Installation

### Backend
```bash
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload

### frontend
cd frontend
npm install
npm start

### API Usage
Endpoint
POST /recommend/

### Sample JSON
{
  "user_id": "user_1",
  "product_name": "Argan Hair Oil",
  "top_n": 5
}

🧪 Metrics Evaluated
Precision@5

Recall@5

Mean Reciprocal Rank (MRR)

👨‍💻 Developed By
Chirag
Machine Learning Intern
Streamline Beauty India Pvt. Ltd.
