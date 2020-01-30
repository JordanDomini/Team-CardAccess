from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()

# A class for objects of type LabMachine that extends the built in base class of sqlalchemy
# Creates a template for sqlalchemy to map db info to an object, making it much more usable
class LabMachine(Base):
    __tablename__ = 'machines'

    Name = Column(String(50), nullable=False)
    Mach_num = Column(String(50), nullable=False, primary_key=True)
    Current_user = Column(Integer, nullable=True)

    def __repr__(self):
        return "<LabMachine(Name=%s , Mach_num='%s', Current_user='%s')>" % (self.Name, self.Mach_num, self.Current_user)


