from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class SubscriptionBaseSchema(BaseModel):
    restaurant_id: str
    name: str
    duration: int
    type: str
    cost: float

class SubscriptionSchema(SubscriptionBaseSchema):
    class Config():
        from_attributes = True

class ShowSubscription(BaseModel):
    restaurant_id: str
    name: str
    duration: int
    type: str
    cost: float
    createdAt: datetime

    class Config():
        from_attributes = True
