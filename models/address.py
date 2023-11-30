from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class Type(str, Enum):
    HOME = "HOME"
    WORK = "WORK"
    REGULAR = "REGULAR"

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    house_no = Column(String, index=True)
    street1 = Column(String, index=True)
    street2 = Column(String, index=True, nullable=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)
    postal_code = Column(Integer, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    type = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    user = relationship("User", back_populates="address", foreign_keys=[user_id])
    restaurant = relationship("Restaurant", back_populates="addresses")


@event.listens_for(Address, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
