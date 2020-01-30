import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# A class for objects of type Admin that extends User
# Creates a template for sqlalchemy to map db info to an object, making it much more usable
class Admin(User):
    __tablename__ = 'admins'

    Num = Column(Integer, primary_key=True)
    Type = Column(Integer, ForeignKey("users.Type"), nullable=False)
    id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return "<Admin(Num=%s , name='%s', rfid_tag='%s', active=%s)>" % (self.Num, self.Type, self.id)