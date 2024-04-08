from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_debts():
    return {"message": "Retrieve all debts"}

@router.post("/")
async def add_debt():
    return {"message": "Add a new debt"}
