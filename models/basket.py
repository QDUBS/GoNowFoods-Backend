from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class Basket(Base):
    __tablename__ = 'baskets'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    createdAt = Column(DateTime, index=True)

    user = relationship("User", back_populates="baskets")
    restaurant = relationship("Restaurant", back_populates="baskets")
    basket_dishes = relationship(
        "BasketDish", back_populates="basket", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)


@event.listens_for(Basket, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
