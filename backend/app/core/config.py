from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")
    
DATABASE_URL = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@devasy23.a8hxla5.mongodb.net/?retryWrites=true&w=majority&appName=Devasy23"
DATABASE_NAME = "Pwallet"
client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]


def get_database() -> AsyncIOMotorClient:
    return db
