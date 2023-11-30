from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
from .address import ShowAddress


class RestaurantBaseSchema(BaseModel):
    user_id: str
    name: str
    image: str
    delivery_fee: float
    min_delivery_time: int
    max_delivery_time: int
    isActive: bool

class RestaurantSchema(RestaurantBaseSchema):
    class Config():
        from_attributes = True

class ShowRestaurant(BaseModel):
    id: str
    user_id: str
    name: str
    image: str
    delivery_fee: float
    min_delivery_time: int
    max_delivery_time: int
    isActive: bool
    createdAt: datetime
    user: ShowUser
    addresses: List[ShowAddress]

    class Config():
        from_attributes = True
