from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object ID")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, v):
        return {
            "title": "ObjectId",
            "type": "string",
            "pattern": "^[0-9a-fA-F]{24}$"
        }

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    username: str
    hashed_password: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
