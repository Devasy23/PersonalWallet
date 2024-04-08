from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_transactions():
    return {"message": "Retrieve all transactions"}

@router.post("/")
async def add_transaction():
    return {"message": "Add a new transaction"}
