from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
# from .order import ShowOrder
from .restaurant import ShowRestaurant


class ShowOrder(BaseModel):
    user_id: str
    courier_id: str
    restaurant_id: str
    total: float
    status: str
    createdAt: datetime
    user: ShowUser
    restaurant: ShowRestaurant
    
class CourierBaseSchema(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    mobile_number: str
    photo: str
    transportation_mode: str
    rating: float

class CourierSchema(CourierBaseSchema):
    class Config():
        from_attributes = True

class ShowCourier(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    mobile_number: str
    photo: str
    transportation_mode: str
    rating: float
    createdAt: datetime
    user: ShowUser
    address: ShowRestaurant
    orders: ShowOrder

    class Config():
        from_attributes = True
