from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "your_database_name"
client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]

def get_database() -> AsyncIOMotorClient:
    return db
