# from sqlalchemy import Column, ForeignKey, String, DateTime, Enum, Float, event
# from sqlalchemy.orm import relationship
# from db.database import Base
# from datetime import datetime
# import uuid


# class TransportationMode(str, Enum):
#     DRIVING = "DRIVING"
#     CYCLING = "CYCLING"

# class Courier(Base):
#     __tablename__ = 'couriers'

#     id = Column(String, primary_key=True, index=True)
#     user_id = Column(String, ForeignKey('users.id'))
#     first_name = Column(String, index=True)
#     last_name = Column(String, index=True)
#     mobile_number = Column(String, index=True)
#     photo = Column(String, index=True)
#     transportation_mode = Column(
#         String, index=True, default=TransportationMode.DRIVING)
#     rating = Column(Float, index=True)
#     createdAt = Column(DateTime, index=True)
#     updatedAt = Column(DateTime, index=True)

#     user = relationship("User", uselist=False, back_populates="courier")
#     address = relationship(
#         "Address", uselist=False, back_populates="courier", cascade="all, delete-orphan")
#     order = relationship(
#         "Order", uselist=False, back_populates="courier", cascade="all, delete-orphan")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.id = str(uuid.uuid4().hex)


# @event.listens_for(Courier, 'before_insert')
# def set_date_before_insert(mapper, connection, target):
#     target.createdAt = datetime.utcnow()
#     target.updatedAt = datetime.utcnow()


# @event.listens_for(Courier, 'before_update')
# def set_updatedAt_before_update(mapper, connection, target):
#     target.updatedAt = datetime.utcnow()
