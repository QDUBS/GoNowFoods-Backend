from sqlalchemy import Column, String, DateTime, event
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime
from enum import Enum
import uuid

class UserType(str, Enum):
    USER = "USER"
    COURIER = "COURIER"
    ENTERPRISE = "ENTERPRISE"

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    user_type = Column(String, index=True, default=UserType.USER)
    createdAt = Column(DateTime, index=True)

    profile = relationship("Profile", uselist=False, back_populates="user", cascade="all, delete-orphan")
    address = relationship("Address", uselist=False, back_populates="user")
    restaurants = relationship(
        "Restaurant", back_populates="user", cascade="all, delete-orphan")
    baskets = relationship(
        "Basket", back_populates="user", cascade="all, delete-orphan")
    orders = relationship(
        "Order", back_populates="user", cascade="all, delete-orphan")
    favorites = relationship(
        "Favorite", back_populates="user", cascade="all, delete-orphan")
    promotions = relationship("Promotion", secondary="user_promotion", back_populates="users")
    support_tickets = relationship("SupportTicket", back_populates="user", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4().hex)

    @property
    def profile_data(self):
        if self.profile is None:
            return None
        return self.profile
    
    @property
    def address_data(self):
        if self.address is None:
            return None
        return self.address


@event.listens_for(User, 'before_insert')
def set_date_before_insert(mapper, connection, target):
    target.createdAt = datetime.utcnow()
