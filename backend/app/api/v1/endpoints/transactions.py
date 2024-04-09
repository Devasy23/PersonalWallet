from fastapi import APIRouter, HTTPException, Body, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from core.config import get_database
from bson import ObjectId
from models.user import PyObjectId
import schemas.transaction as transaction_schema

router = APIRouter()

async def get_db_client() -> AsyncIOMotorClient:
    return get_database()

@router.get("/", response_model=List[transaction_schema.Transaction]) # 
async def get_transactions(db: AsyncIOMotorClient = Depends(get_db_client)):
    transactions = await db["transactions"].find().to_list(1000)
    return transactions

@router.post("/", response_model=transaction_schema.Transaction) 
async def add_transaction(transaction: transaction_schema.TransactionCreate, db: AsyncIOMotorClient = Depends(get_db_client)):
    transaction_dict = transaction.dict(by_alias=True)
    result = await db["transactions"].insert_one(transaction_dict)
    if result.inserted_id:
        return await db["transactions"].find_one({"_id": result.inserted_id})
    raise HTTPException(status_code=400, detail="Error adding transaction.")

@router.get("/account/{account_id}", response_model=List[transaction_schema.Transaction])
async def get_all_transactions_for_account(account_id: PyObjectId, db: AsyncIOMotorClient = Depends(get_db_client)):
    transactions = await db["transactions"].find({"account_id": account_id}).to_list(1000)
    return transactions
