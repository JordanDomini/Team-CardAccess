import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = declarative_base()

class Admin(User):
    __tablename__ = 'admins'

    Num = Column(Integer, primary_key=True)
    Type = Column(Integer, ForeignKey("users.Type"), nullable=False)
    id = Column(Integer, ForeignKey("users.id"), nullable=False)