# 🚀 NLP REST API using FastAPI | Production-Ready AI Service

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Framework](https://img.shields.io/badge/Framework-FastAPI-green)
![NLP](https://img.shields.io/badge/NLP-Transformers-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project converts multiple NLP models into a **REST API service** using FastAPI.

Instead of building a standalone script or UI-only app, this project exposes AI capabilities as API endpoints — following real-world production architecture.

---

## 📌 Project Overview

This API provides the following AI services:

- Sentiment Analysis  
- Text Summarization  
- Text Generation  

All powered by pretrained Transformer models from HuggingFace.

The API can be integrated with:

- Web applications  
- Mobile apps  
- Frontend frameworks (React, Angular, etc.)  
- External systems  

---

## 🎯 Project Objective

The goal of this project is to:

✅ Convert NLP models into REST API endpoints  
✅ Use FastAPI for production-ready backend  
✅ Return structured JSON responses  
✅ Demonstrate real-world AI backend architecture  

---

## 🧠 Available Endpoints

### 🔹 1. Sentiment Analysis
**POST** `/sentiment`

Request:
```json
{
  "text": "I love AI!"
}
Response:

{
  "label": "POSITIVE",
  "confidence": 0.998
}
🔹 2. Text Summarization
POST /summarize

Request:

{
  "text": "Long paragraph here..."
}
Response:

{
  "summary": "Short summarized version."
}
🔹 3. Text Generation
POST /generate

Request:

{
  "text": "Artificial Intelligence is"
}
Response:

{
  "generated_text": "Artificial Intelligence is transforming industries..."
}
🏗 System Architecture
Client (Frontend / Postman)
            ↓
        FastAPI Server
            ↓
    Transformer Models
            ↓
        JSON Response
This mirrors real AI SaaS backend architecture.

📂 Project Structure
Day23_NLP_REST_API/
│
├── app.py
└── README.md
⚙️ Technologies Used
Python 🐍

FastAPI

Uvicorn

HuggingFace Transformers

PyTorch

▶️ How to Run
Step 1 — Install dependencies
pip install fastapi uvicorn transformers torch
Step 2 — Start the API server
uvicorn app:app --reload
Step 3 — Open API Docs
Visit:

http://127.0.0.1:8000/docs
FastAPI automatically provides interactive Swagger documentation.

🚀 Learning Outcomes
By completing this project, you will:

✔ Convert AI models into API services
✔ Build production-style backend systems
✔ Work with JSON-based communication
✔ Understand scalable AI architecture
✔ Move from project-level AI → infrastructure-level AI

🌍 Real-World Applications
This architecture is used in:

AI SaaS platforms

Enterprise AI services

Customer support systems

Content automation tools

AI-powered applications

👨‍💻 Author
Harsh Chauhan
Computer Engineering Student
AI & NLP Enthusiast

