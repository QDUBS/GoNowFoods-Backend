from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class AdvertBaseSchema(BaseModel):
    restaurant_id: str
    name: str
    image: str
    duration: int
    status: str

class AdvertSchema(AdvertBaseSchema):
    class Config():
        from_attributes = True

class ShowAdvert(BaseModel):
    restaurant_id: str
    name: str
    image: str
    duration: int
    status: str
    createdAt: datetime

    class Config():
        from_attributes = True
