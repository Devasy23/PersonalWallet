import models.user as user_model
import schemas.user as user_schema
from bson import ObjectId
from core.config import get_database
from fastapi import APIRouter, Body, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from werkzeug.security import check_password_hash, generate_password_hash

router = APIRouter()


async def get_db_client() -> AsyncIOMotorClient:
    return get_database()


@router.post("/register", response_description="User added to the database")
async def register(
    user: user_schema.UserCreate, db: AsyncIOMotorClient = Depends(get_db_client)
):
    user_dict = user.dict()
    user_dict["hashed_password"] = generate_password_hash(user_dict["password"])
    del user_dict["password"]  # Remove plain password
    result = await db["users"].insert_one(user_dict)
    if result.inserted_id:
        return {"_id": str(result.inserted_id)}
    raise HTTPException(status_code=400, detail="Error registering user.")


@router.post("/login")
async def login(
    user: user_schema.UserLogin, db: AsyncIOMotorClient = Depends(get_db_client)
):
    db_user = await db["users"].find_one({"username": user.username})
    if db_user and check_password_hash(db_user["hashed_password"], user.password):
        return {"message": "User authenticated successfully"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
