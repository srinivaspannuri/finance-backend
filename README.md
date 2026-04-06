# 💰 Finance Backend API

A backend API built using FastAPI to manage users and financial transactions.

## 🚀 Live Demo
https://finance-backend-1-d0rc.onrender.com/docs

## 🛠 Tech Stack
- Python
- FastAPI
- Uvicorn
- Render (Deployment)

## 📌 Features
- Get Users
- Add Users
- Get Transactions
- Add Transactions
- Dashboard (Income, Expense, Balance)

## 📂 API Endpoints

### 🧑 Users
- GET /users → Get all users
- POST /users → Add new user

### 💸 Transactions
- GET /transactions → Get all transactions
- POST /transactions → Add transaction

### 📊 Dashboard
- GET /dashboard → Get income, expense, balance

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
