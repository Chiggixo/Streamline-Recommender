# 💇‍♀️ Streamline Recommender – Smart Product Recommendation System for Salon Professionals

![GitHub stars](https://img.shields.io/github/stars/Chiggixo/Streamline-Recommender?style=social)
![License](https://img.shields.io/github/license/Chiggixo/Streamline-Recommender)

An AI-powered recommendation system built for Streamline Beauty India Pvt. Ltd. to suggest personalized salon products based on user behavior, product metadata, and content similarity.
Internship Project | Streamline Beauty India Pvt. Ltd.
Intern: Chirag  
Domain: Machine Learning & Full Stack Integration  
Duration: 45 Days

## 🔧 Tech Stack

| Layer              | Technology                                                        |
| ------------------ | ----------------------------------------------------------------- |
| **Frontend**       | React.js (with dropdown UI, form, cards)                          |
| **Backend**        | FastAPI (Python 3.10)                                             |
| **Database**       | CSV files (`beauty_product_ratings.csv`, `product_metadata.json`) |
| **Recommendation** | Hybrid (Collaborative + Content-based filtering)                  |
| **Hosting**        | Netlify (frontend) + Render (backend)                             |

---

## 🖼️ Features

* 🔍 Personalized Product Recommendations
* 🧠 Hybrid AI Recommender (Cold-start support)
* 📥 Admin Panel: Add/Update products with metadata
* 📊 Real-time score display
* 🧪 Persona-based testing supported
* 📦 Deployed frontend + backend with live API

---

## 🚀 Live Demo Links

| Service        | URL                                                     |
| -------------- | ------------------------------------------------------- |
| 🔗 Frontend    | [Netlify Live](https://streamline-beauty-recommendation.netlify.app/)    |
| 🔌 Backend API | [Swagger UI](https://your-render-api.onrender.com/docs) |

---

## 📸 Screenshots

### ✅ Recommendation UI

![Recommendation]

### 🧑‍💼 Admin Panel

![Admin Panel]

### 🧪 Swagger API

![Swagger]

---

## 🧑‍💻 Local Development Setup

```bash
# 1. Clone the repository
https://github.com/Chiggixo/Streamline-Recommender.git

# 2. Backend Setup (FastAPI)
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# 3. Frontend Setup (React)
cd frontend
npm install
npm start
```

---

## 📁 Folder Structure

```
product-recommender/
├── backend/                 # FastAPI backend (APIs, logic, admin)
├── frontend/                # React frontend (user + admin)
├── data/                    # CSV + product metadata
├── src/                     # Recommender logic (hybrid, fallback, etc.)
```

---

## ✅ Future Features

* ⭐ User rating submission interface
* 🧾 Product category + brand filtering
* 🔒 JWT-based Admin Auth
* 📊 Analytics for most recommended products

---

## 🙌 Acknowledgements

Built with ❤️ during internship at **Streamline Beauty India Pvt. Ltd** by **Chirag**.

> For feedback, contact: [Chiggixo on GitHub](https://github.com/Chiggixo)

---

🧪 Metrics Evaluated
Run the evaluator:
python -m src.evaluation

Average Precision@5: 0.42
Average Recall@5: 0.88
Average MRR: 0.35


👨‍💻 Intern
Name: Chirag
Role: Machine Learning Intern
College: Sharda University
Company: Streamline Beauty India Pvt. Ltd.

## 📃 License

[MIT License](LICENSE)
