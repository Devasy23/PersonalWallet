from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_accounts():
    return {"message": "Retrieve all accounts"}

@router.post("/")
async def add_account():
    return {"message": "Add a new account"}
