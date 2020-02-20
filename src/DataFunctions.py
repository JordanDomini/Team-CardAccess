#!/usr/bin/env python
import Student
import Admin
import User
from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
mach_num = "MACH001"
user_id = "none"
PWD='123123123'
USR='test_user'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@10.250.250.250/test_db'.format(USR, PWD)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

# checks permissions of student or just if admin
def check_user_permission(scanned_tag):
    session = Session()
    req_user = session.query(Student).filter_by(rfid_tag=scanned_tag).first
    if req_user is not null:
        if exec("req_user.$s" % mach_num):
            return True
        else:
            return False
    req_user = session.query(Admin).filter_by(rfid_tag=scanned_tag).first
    if req_user is not null:
        return True
    return False

# checks the user type
def check_user_level(scanned_tag):
    session = Session()
    req_user = session.query(User).filter_by(rfid_tag=scanned_tag).first
    return req_user.Type

# gets user
def get_user(scanned_tag):
    session = Session()
    type = check_user_level(scanned_tag)
    if type == 0:
        return session.query(Student).filter_by(rfid_tag=scanned_tag)
    elif type > 0:
        return session.query(Admin).filter_by(rfid_tag=scanned_tag)

# adds user to db using an existing object
def addUser(user_info):
    session = Session()
    session.add(user_info)
    session.commit()
    return True

# edit the rfid tag of an existing user
def edit_rfid_tag(id_num):
    session = Session()    # starts the connected session
    type = check_user_level()    # checks the user's type
    if type == 0:    # for type student
        # mapper query to filter by id number and get first result
        req_user = session.query(Student).filter_by(id=id_num).first
    else:     # for admin
        # mapper query to filter by id number and get first result
        req_user = session.query(Admin).filter_by(id=id_num).first
    while True:  # making an infinite loop
        id, text = reader.read()  # waiting for id to be scanned
        if reader.read():
            id, string = reader.read()  # gets the rfid tag
            req_user.rfid_tag = str(id).strip() # assigns the tag to the user profile
            session.commit()   # commits the changes
            break # breaks infinite loop
