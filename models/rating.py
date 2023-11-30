from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    dish_id = Column(String, ForeignKey('dishes.id'))
    rating_no = Column(Integer, index=True)
    comment = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    user = relationship("User", back_populates="ratings", foreign_keys=[user_id])
    restaurant = relationship("Restaurant", back_populates="ratings")
    dish = relationship("Dish", back_populates="ratings")


@event.listens_for(Rating, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
