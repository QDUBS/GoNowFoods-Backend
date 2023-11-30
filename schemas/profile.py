from typing import List
from pydantic import BaseModel
from datetime import datetime
from .user import ShowUser


class ProfileBaseSchema(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    mobile_number: str
    photo: str

class ProfileSchema(ProfileBaseSchema):
    class Config():
        from_attributes = True

class ShowProfile(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    mobile_number: str
    photo: str
    createdAt: datetime
    user: ShowUser

    class Config():
        from_attributes = True
