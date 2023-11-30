from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .restaurant import ShowRestaurant
from .dish import ShowDish


class FavoriteBaseSchema(BaseModel):
    user_id: str
    restaurant_id: str
    dish_id: str
    type: str

class FavoriteSchema(FavoriteBaseSchema):
    class Config():
        from_attributes = True

class ShowFavorite(BaseModel):
    user_id: str
    restaurant_id: str
    dish_id: str
    type: str
    createdAt: datetime
    restaurant: ShowRestaurant
    dish: ShowDish

    class Config():
        from_attributes = True
