from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class Type(str, Enum):
    ONGOING = "ONGOING"
    EXPIRED = "EXPIRED"


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    name = Column(String, index=True, unique=True)
    duration = Column(Integer, index=True) # In days
    type = Column(String, index=True)
    cost = Column(Float, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    restaurant = relationship("Restaurant", back_populates="subscriptions")


@event.listens_for(Subscription, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
