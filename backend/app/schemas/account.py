from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.pyobjectid import PyObjectId

class AccountBase(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')
    user_id: PyObjectId = Field(default_factory=PyObjectId)
    type: str
    balance: float

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: lambda oid: str(oid)}


class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')