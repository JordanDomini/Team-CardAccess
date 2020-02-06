from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = declarative_base()


# A class for objects of type Student that extends User
# Creates a template for sqlalchemy to map db info to an object, making it much more usable
class Student(Base):
    __tablename__ = 'students'

    Num = Column(Integer, primary_key=True, index=True)
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
    User = relationship('users', )

    def __repr__(self):
        return "<Student(Num=%s , Type='%s', Mach001='%s', Mach002=%s, Mach003='%s', Mach004='%s', Mach005='%s', " \
               "Mach006='%s', Mach007='%s', Mach008='%s', Mach009='%s', Mach010='%s')>" % \
               (self.Num, self.Type, self.Mach001, self.Mach002, self.Mach003, self.Mach004, self.Mach005, self.Mach006,
                self.Mach007, self.Mach008, self.Mach009, self.Mach010)
