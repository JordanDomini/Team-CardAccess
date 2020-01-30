from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rfid_tag = Column(String(50), unique=True, nullable=False)
    Type = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<User(id=%s , name='%s', rfid_tag='%s', active=%s)>" % (self.id, self.name, self.rfid_tag, self.active)

    def get_user_name(self):
        return self.user_name

    def get_user_id(self):
        return self.user_id

    def get_rfid_tag(self):
        return self.rfid_tag

    def get_type(self):
        return self.type_num

