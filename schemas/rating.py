from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .restaurant import ShowRestaurant
from .dish import ShowDish


class RatingBaseSchema(BaseModel):
    user_id: str
    restaurant_id: str
    dish_id: str
    rating_no: int
    comment: str

class RatingSchema(RatingBaseSchema):
    class Config():
        from_attributes = True

class ShowRating(BaseModel):
    user_id: str
    restaurant_id: str
    dish_id: str
    rating_no: int
    comment: str
    createdAt: datetime
    restaurant: ShowRestaurant
    dish: ShowDish

    class Config():
        from_attributes = True
