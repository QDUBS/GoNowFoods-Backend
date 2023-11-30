from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class OrderDish(Base):
    __tablename__ = 'order_dishes'

    id = Column(String, primary_key=True, index=True)
    dish_id = Column(String, ForeignKey('dishes.id'))
    order_id = Column(String, ForeignKey('orders.id'))
    quantity = Column(Integer, index=True)
    createdAt = Column(DateTime, index=True)

    dish = relationship("Dish", back_populates="order_dish")
    order = relationship("Order", back_populates="order_dishes")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)


@event.listens_for(OrderDish, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
