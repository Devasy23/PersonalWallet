# app.py
from fastapi import FastAPI

def include_routers(app: FastAPI, routers: list) -> None:
    for router in routers:
        app.include_router(router['router'], prefix=router['prefix'], tags=router['tags'])

# main.py
import uvicorn
from app import include_routers
from api.v1.endpoints import user, transactions, debts, accounts

app = FastAPI()

routers = [
    {'router': user.router, 'prefix': '/api/v1/user', 'tags': ['User']},
    {'router': transactions.router, 'prefix': '/api/v1/transactions', 'tags': ['Transactions']},
    {'router': debts.router, 'prefix': '/api/v1/debts', 'tags': ['Debts']},
    {'router': accounts.router, 'prefix': '/api/v1/accounts', 'tags': ['Accounts']}
]

include_routers(app, routers)

if __name__ == "__main__":