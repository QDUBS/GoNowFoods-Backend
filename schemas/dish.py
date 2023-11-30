from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
from .restaurant import ShowRestaurant


class DishBaseSchema(BaseModel):
    restaurant_id: str
    name: str
    image: str
    description: str
    price: float
    category: str
    category_code: str

class DishSchema(DishBaseSchema):
    class Config():
        from_attributes = True

class ShowDish(BaseModel):
    id: str
    restaurant_id: str
    name: str
    image: str
    description: str
    price: float
    category: str
    category_code: str
    createdAt: datetime

    class Config():
        from_attributes = True
