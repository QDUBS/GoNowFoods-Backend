# association.py
from sqlalchemy import Table, Column, String, ForeignKey
from db.database import Base

user_promotion = Table('user_promotion', Base.metadata,
    Column('user_id', String, ForeignKey('users.id')),
    Column('promotion_id', String, ForeignKey('promotions.id'))
)
