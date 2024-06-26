# transaction_schema.py
from typing import Optional

from bson import ObjectId
from models.pyobjectid import PyObjectId
from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    account_id: PyObjectId = Field(default_factory=PyObjectId)
    date: str
    type: str
    method: str
    amount: float
    description: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: lambda oid: str(oid)}


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    # id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: lambda oid: str(oid)}

    # pass
