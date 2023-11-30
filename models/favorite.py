from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class Type(str, Enum):
    RESTAURANT = "RESTAURANT"
    DISH = "DISH"


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    dish_id = Column(String, ForeignKey('dishes.id'))
    type = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    restaurant = relationship("Restaurant", uselist=False, back_populates="favorite")
    dish = relationship("Dish", uselist=False, back_populates="favorite")
    user = relationship("User", back_populates="favorites")


@event.listens_for(Favorite, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
