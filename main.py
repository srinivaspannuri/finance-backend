from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Finance Backend API")

# --------- Models ---------
class User(BaseModel):
    id: int
    name: str

class Transaction(BaseModel):
    id: int
    amount: float
    type: str

# --------- Dummy Data ---------
users = []
transactions = []

# --------- APIs ---------

@app.get("/")
def home():
    return {"message": "Finance Backend Running 🚀"}

# USERS
@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users")
def add_user(user: User):
    users.append(user)
    return {"message": "User added successfully"}

# TRANSACTIONS
@app.get("/transactions", response_model=List[Transaction])
def get_transactions():
    return transactions

@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transactions.append(transaction)
    return {"message": "Transaction added successfully"}

# DASHBOARD
@app.get("/dashboard")
def dashboard():
    total_income = sum(t.amount for t in transactions if t.type == "credit")
    total_expense = sum(t.amount for t in transactions if t.type == "debit")
    balance = total_income - total_expense

    return {
        "income": total_income,
        "expense": total_expense,
        "balance": balance
}
