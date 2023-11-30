from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class Status(str, Enum):
    RELEVANT = "RELEVANT"
    IRRELEVANT = "IRRELEVANT"


class Advert(Base):
    __tablename__ = 'adverts'

    id = Column(String, primary_key=True, index=True)
    restaurant_id = Column(String, ForeignKey('restaurants.id'))
    name = Column(String, index=True)
    image = Column(String, index=True)
    duration = Column(Integer, index=True)
    status = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    restaurant = relationship("Restaurant", back_populates="adverts")


@event.listens_for(Advert, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
