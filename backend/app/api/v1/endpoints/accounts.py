from fastapi import APIRouter, HTTPException, Body, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from core.config import get_database
import schemas.account as account_schema

router = APIRouter()

async def get_db_client() -> AsyncIOMotorClient:
    return get_database()

@router.get("/", response_model=List[account_schema.Account])
async def get_accounts(db: AsyncIOMotorClient = Depends(get_db_client)):
    accounts = await db["accounts"].find().to_list(1000)
    return accounts

@router.post("/", response_model=account_schema.Account)
async def add_account(account: account_schema.AccountCreate, db: AsyncIOMotorClient = Depends(get_db_client)):
    account_dict = account.dict(by_alias=True)
    result = await db["accounts"].insert_one(account_dict)
    if result.inserted_id:
        return await db["accounts"].find_one({"_id": result.inserted_id})
    raise HTTPException(status_code=400, detail="Error adding account.")
