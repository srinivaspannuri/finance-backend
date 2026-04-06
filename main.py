from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Finance Backend Running"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ]

@app.get("/transactions")
def get_transactions():
    return [
        {"id": 1, "amount": 1000, "type": "credit"},
        {"id": 2, "amount": 500, "type": "debit"}
    ]

@app.get("/balance")
def get_balance():
    return {"balance": 5000}
