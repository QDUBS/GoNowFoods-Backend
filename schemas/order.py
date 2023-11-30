from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
from .dish import ShowDish
from .restaurant import ShowRestaurant


class ShowOrderDish(BaseModel):
    id: str
    dish_id: str
    order_id: str
    quantity: int
    createdAt: datetime
    dish: ShowDish

    class Config():
        from_attributes = True

class OrderBaseSchema(BaseModel):
    user_id: str
    courier_id: str
    restaurant_id: str
    total: float
    status: str

class OrderSchema(OrderBaseSchema):
    class Config():
        from_attributes = True

class ShowOrder(BaseModel):
    id: str
    code: str
    user_id: str
    courier_id: Optional[str]
    restaurant_id: str
    total: float
    status: str
    payment: str
    createdAt: datetime
    completedAt: datetime
    user: ShowUser
    restaurant: ShowRestaurant
    order_dishes: List[ShowOrderDish]

    class Config():
        from_attributes = True
