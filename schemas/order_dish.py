from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .dish import ShowDish
from .order import ShowOrder


class OrderDishBaseSchema(BaseModel):
    dish_id: str
    order_id: str
    quantity: int

class OrderDishSchema(OrderDishBaseSchema):
    class Config():
        from_attributes = True

class ShowOrderDish(BaseModel):
    id: str
    dish_id: str
    order_id: str
    quantity: int
    createdAt: datetime
    dish: ShowDish
    order: ShowOrder

    class Config():
        from_attributes = True
