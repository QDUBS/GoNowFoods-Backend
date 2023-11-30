from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class AddressBaseSchema(BaseModel):
    user_id: str
    house_no: str
    street1: str
    street2: Optional[str]
    city: str
    state: str
    country: str
    postal_code: int
    latitude: float
    longitude: float
    type: str

class AddressSchema(AddressBaseSchema):
    class Config():
        from_attributes = True

class ShowAddress(BaseModel):
    user_id: str
    house_no: str
    street1: str
    street2: Optional[str]
    city: str
    state: str
    country: str
    postal_code: int
    latitude: float
    longitude: float
    type: str
    createdAt: datetime

    class Config():
        from_attributes = True
