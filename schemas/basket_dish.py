from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
from .dish import ShowDish


class BasketDishBaseSchema(BaseModel):
    basket_id: str
    dish_id: str
    quantity: int

class BasketDishSchema(BasketDishBaseSchema):
    class Config():
        from_attributes = True

class ShowBasketDish(BaseModel):
    id: str
    basket_id: str
    dish_id: str
    quantity: int
    createdAt: datetime
    dish: ShowDish

    class Config():
        from_attributes = True
