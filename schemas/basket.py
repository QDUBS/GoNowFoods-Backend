from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser
from .restaurant import ShowRestaurant
from .basket_dish import ShowBasketDish

class BasketBaseSchema(BaseModel):
    user_id: str
    restaurant_id: str

class BasketSchema(BasketBaseSchema):
    class Config():
        from_attributes = True

class ShowBasket(BaseModel):
    id: str
    user_id: str
    restaurant_id: str
    createdAt: datetime
    basket_dishes: List[ShowBasketDish]
    restaurant: ShowRestaurant

    class Config():
        from_attributes = True
