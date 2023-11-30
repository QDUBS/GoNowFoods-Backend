from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class PromotionBaseSchema(BaseModel):
    name: str
    description: str
    duration: int
    status: str
    code: str
    cost: float
    percentage: int
    count: int

class PromotionSchema(PromotionBaseSchema):
    class Config():
        from_attributes = True

class ShowPromotion(BaseModel):
    name: str
    description: str
    duration: int
    status: str
    code: str
    cost: float
    percentage: int
    count: int
    createdAt: datetime

    class Config():
        from_attributes = True
