from fastapi import APIRouter
from werkzeug.security import check_password_hash, generate_password_hash
from pymongo import MongoClient

router = APIRouter()

@router.post("/register")
async def register_user():
    return {"message": "User registration endpoint"}

@router.post("/login")
async def login_user():
    return {"message": "User login endpoint"}
