from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    name = Column(String, index=True)
    image = Column(String, index=True)
    description = Column(Text, index=True)
    price = Column(Float, index=True)
    category = Column(String, index=True)
    category_code = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    restaurant = relationship("Restaurant", back_populates="dishes")
    basket_dish = relationship("BasketDish", uselist=False,
                               back_populates="dish", cascade="all, delete-orphan")
    order_dish = relationship("OrderDish", uselist=False,
                               back_populates="dish", cascade="all, delete-orphan")
    favorite = relationship(
        "Favorite", back_populates="dish", cascade="all, delete-orphan")


@event.listens_for(Dish, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
