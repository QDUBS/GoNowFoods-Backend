from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class Status(str, Enum):
    ONGOING = "ONGOING"
    EXPIRED = "EXPIRED"


class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, index=True)
    duration = Column(Integer, index=True) # In days
    status = Column(String, index=True)
    code = Column(String, index=True, unique=True)
    cost = Column(Float, index=True)
    percentage = Column(Integer, index=True)
    count = Column(Integer, index=True)
    createdAt = Column(DateTime, index=True)

    users = relationship("User", secondary="user_promotion", back_populates="promotions")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)


@event.listens_for(Promotion, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
