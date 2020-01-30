from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()

class LabMachine(Base):
    __tablename__ = 'machines'

    Name = Column(String(50), nullable=False, )

