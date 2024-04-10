from typing import Optional

from models.pyobjectid import PyObjectId
from pydantic import BaseModel, Field


class DebtBase(BaseModel):
    amount: float
    status: str  # Example values: "unpaid", "paid"
    description: Optional[str] = None


class DebtCreate(DebtBase):
    debtor_id: PyObjectId


class Debt(DebtBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    debtor_id: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
