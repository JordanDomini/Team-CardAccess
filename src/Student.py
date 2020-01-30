import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = declarative_base()


class Student(User):
    __tablename__ = 'students'

    Num = Column(Integer, primary_key=True)
    Type = Column(Integer, ForeignKey("users.Type"), nullable=False)
    Mach001 = Column(Boolean, nullable=False)
    Mach002 = Column(Boolean, nullable=False)
    Mach003 = Column(Boolean, nullable=False)
    Mach004 = Column(Boolean, nullable=False)
    Mach005 = Column(Boolean, nullable=False)
    Mach006 = Column(Boolean, nullable=False)
    Mach007 = Column(Boolean, nullable=False)
    Mach008 = Column(Boolean, nullable=False)
    Mach009 = Column(Boolean, nullable=False)
    Mach010 = Column(Boolean, nullable=False)
    id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return "<Student(id=%s , name='%s', rfid_tag='%s', active=%s)>" % (self.Num, self.Type, self.rfid_tag, self.active)
