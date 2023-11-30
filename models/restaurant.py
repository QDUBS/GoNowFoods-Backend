from sqlalchemy import Boolean, Column, String, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    name = Column(String, index=True)
    image = Column(String, index=True)
    delivery_fee = Column(Float, index=True)
    min_delivery_time = Column(Integer, index=True)
    max_delivery_time = Column(Integer, index=True)
    # rating = Column(Float, index=True)
    isActive = Column(Boolean, index=True, default=False)
    createdAt = Column(DateTime, index=True)

    user = relationship("User", back_populates="restaurants")
    addresses = relationship("Address", back_populates="restaurant")
    dishes = relationship(
        "Dish", back_populates="restaurant", cascade="all, delete-orphan")
    baskets = relationship(
        "Basket", back_populates="restaurant", cascade="all, delete-orphan")
    orders = relationship(
        "Order", back_populates="restaurant", cascade="all, delete-orphan")
    adverts = relationship(
        "Advert", back_populates="restaurant", cascade="all, delete-orphan")
    favorite = relationship(
        "Favorite", back_populates="restaurant", cascade="all, delete-orphan")
    subscriptions = relationship(
        "Subscription", back_populates="restaurant", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex) 


@event.listens_for(Restaurant, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
