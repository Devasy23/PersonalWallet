# File: debts.py within your /app/api/v1/endpoints directory

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from models.pyobjectid import PyObjectId
from core.config import get_database
import schemas.debt as debt_schema

router = APIRouter()

@router.post("/", response_model=debt_schema.Debt)
async def add_debt(debt: debt_schema.DebtCreate, db: AsyncIOMotorClient = Depends(get_database)):
    debt_dict = debt.dict(by_alias=True)
    result = await db["debts"].insert_one(debt_dict)
    if result.inserted_id:
        return await db["debts"].find_one({"_id": result.inserted_id})
    raise HTTPException(status_code=400, detail="Error adding debt.")

@router.get("/", response_model=List[debt_schema.Debt])
async def get_debts(db: AsyncIOMotorClient = Depends(get_database)):
    debts = await db["debts"].find().to_list(1000)
    return debts

@router.get("/{debt_id}", response_model=debt_schema.Debt)
async def get_debt(debt_id: PyObjectId, db: AsyncIOMotorClient = Depends(get_database)):
    debt = await db["debts"].find_one({"_id": debt_id})
    if debt:
        return debt
    else:
        raise HTTPException(status_code=404, detail="Debt not found")
