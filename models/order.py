from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid


class OrderStatus(str, Enum):
    NEW = "NEW"
    IN_PREPARATION = "IN_PREPARATION"
    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    ACCEPTED = "ACCEPTED"
    PICKED_UP = "PICKED_UP"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class OrderPayment(str, Enum):
    CASH = "CASH"
    CARD = "CARD"
    POS = "POS"
    TRANSFER = "TRANSFER"


class Order(Base):
    __tablename__ = 'orders'

    id = Column(String, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    courier_id = Column(String, nullable=True)
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    total = Column(Float, index=True)
    status = Column(String, index=True, default=OrderStatus.NEW)
    payment = Column(String, index=True, default=OrderPayment.CASH)
    createdAt = Column(DateTime, index=True)
    completedAt = Column(DateTime, index=True)

    user = relationship("User", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    order_dishes = relationship(
        "OrderDish", back_populates="order", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)
        self.code = self.generate_order_code()

    def generate_order_code(self):
        return f'G0{uuid.uuid4().hex[:4]}'


@event.listens_for(Order, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
    if not target.code:
        target.code = target.generate_order_code()
