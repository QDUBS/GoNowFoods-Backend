from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class ShowProfile(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    mobile_number: str
    photo: str
    createdAt: datetime

    class Config():
        from_attributes = True

class ShowAddress(BaseModel):
    user_id: str
    house_no: str
    street1: str
    street2: str
    city: str
    state: str
    country: str
    postal_code: int
    latitude: float
    longitude: float
    createdAt: datetime

    class Config():
        from_attributes = True

class UserSchema(BaseModel):
    email: str
    password: str
    user_type: str

class UpdateUserSchema(BaseModel):
    email: str

    class Config():
        from_attributes = True

class CreateUser(BaseModel):
    id: str
    email: str

    class Config():
        from_attributes = True

class ShowUser(BaseModel):
    id: str
    email: str
    user_type: str
    profile_data: Union[ShowProfile, None]
    address_data: Union[ShowAddress, None]

    class Config():
        from_attributes = True
