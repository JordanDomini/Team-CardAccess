from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


# A class for objects of type student that extends User
# Creates a template for sqlalchemy to map db info to an object, making it much more usable
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rfid_tag = Column(String(50), unique=True, nullable=False)
    Type = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<User(id=%s , name='%s', rfid_tag='%s', active=%s)>" % (self.id, self.name, self.rfid_tag, self.active)

class Student(Base):
    __tablename__ = 'students'

    Num = Column(Integer, primary_key=True, autoincrement=True)
    Type = Column(Integer, nullable=False)
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
    user = relationship("User", backref=backref("student", uselist=False))

    def __repr__(self):
        return "<Student(Num=%s , Type='%s', Mach001='%s', Mach002=%s, Mach003='%s', Mach004='%s', Mach005='%s', " \
               "Mach006='%s', Mach007='%s', Mach008='%s', Mach009='%s', Mach010='%s')>" % \
               (self.Num, self.Type, self.Mach001, self.Mach002, self.Mach003, self.Mach004, self.Mach005, self.Mach006,
                self.Mach007, self.Mach008, self.Mach009, self.Mach010)


class Admin(Base):
    __tablename__ = 'admins'

    Num = Column(Integer, primary_key=True)
    Type = Column(Integer, nullable=False)
    id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref=backref("admin", uselist=False))

    def __repr__(self):
        return "<Admin(Num=%s , name='%s', rfid_tag='%s')>" % (self.Num, self.Type, self.id)


class LabMachine(Base):
    __tablename__ = 'machines'

    Name = Column(String(50), nullable=False)
    Mach_num = Column(Integer, nullable=False, primary_key=True, index=True)
    Current_user = Column(Integer, nullable=True)

    def __repr__(self):
        return "<LabMachine(Name=%s , Mach_num='%s', Current_user='%s')>" % (
            self.Name, self.Mach_num, self.Current_user)


# fo = open("/home/pi/Mach_Number.txt")
# mach_num = fo.read().strip()
# PWD = 'Nga4@G&KH64}.knJ'
# # PWD = 'eDVpY%!uQk4V@y6F'
# USR = 'MACH'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@10.250.250.250/test_db'.format(USR, PWD)
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# # Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
