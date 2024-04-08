from fastapi import FastAPI
from api.v1.endpoints import user, transactions, debts, accounts
import uvicorn

# Create the FastAPI app
app = FastAPI()

app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])
app.include_router(debts.router, prefix="/api/v1/debts", tags=["Debts"])
app.include_router(accounts.router, prefix="/api/v1/accounts", tags=["Accounts"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)