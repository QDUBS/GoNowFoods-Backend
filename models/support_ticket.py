from sqlalchemy import Column, String, Text, DateTime, Float, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class Issue(str, Enum):
    ORDER = "ORDER"
    PAYMENT = "PAYMENT"
    DELIVERY = "DELIVERY"

class SupportTicket(Base):
    __tablename__ = 'support_tickets'

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    issue = Column(String, index=True)
    subject = Column(String, index=True)
    message = Column(String, index=True)
    createdAt = Column(DateTime, index=True)

    user = relationship("User", back_populates="support_tickets")


@event.listens_for(SupportTicket, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
