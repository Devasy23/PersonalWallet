import uvicorn
from api.v1.endpoints import accounts, debts, transactions, user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(
    transactions.router, prefix="/api/v1/transactions", tags=["Transactions"]
)
app.include_router(debts.router, prefix="/api/v1/debts", tags=["Debts"])
app.include_router(accounts.router, prefix="/api/v1/accounts", tags=["Accounts"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
