#!/usr/bin/env python
import User
from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker
import time
from mfrc522 import SimpleMFRC522

fo = open("/home/pi/Mach_Number.txt")
reader = SimpleMFRC522()
mach_num = fo.read().strip()
user_id = "none"
PWD = 'Nga4@G&KH64}.knJ'
USR = "MACH"
if mach_num == "MACH":
    IP = 'localhost'
else:
    IP = '10.250.250.250'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/test_db'.format(USR, PWD, IP)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
fo.close()


# checks permissions of student or just if admin
def check_user_permission(scanned_tag):
    session = Session()
    req_user = session.query(User.User).filter_by(rfid_tag=scanned_tag).first()
    req_student = session.query(User.Student).filter_by(id=req_user.id).first()
    if req_student:
        if mach_num == "Mach001":
            if req_student.Mach001:
                return True
            else:
                return False
        elif mach_num == "Mach002":
            if req_student.Mach002:
                return True
            else:
                return False
        elif mach_num == "Mach003":
            if req_student.Mach003:
                return True
            else:
                return False
        elif mach_num == "Mach004":
            if req_student.Mach004:
                return True
            else:
                return False
        elif mach_num == "Mach005":
            if req_student.Mach005:
                return True
            else:
                return False
        elif mach_num == "Mach006":
            if req_student.Mach006:
                return True
            else:
                return False
        elif mach_num == "Mach007":
            if req_student.Mach007:
                return True
            else:
                return False
        elif mach_num == "Mach008":
            if req_student.Mach008:
                return True
            else:
                return False
        elif mach_num == "Mach009":
            if req_student.Mach009:
                return True
            else:
                return False
        elif mach_num == "Mach010":
            if req_student.Mach010:
                return True
            else:
                return False
    req_admin = session.query(User.Admin).filter_by(id=req_user.id).first()
    if req_admin:
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
        return session.query(User.Student).filter_by(rfid_tag=scanned_tag)
    elif type > 0:
        return session.query(User.Admin).filter_by(rfid_tag=scanned_tag)


# adds user to db using an existing object
def addUser(user_info):
    session = Session()
    session.add(user_info)
    session.commit()
    return True


# edit the rfid tag of an existing user
def edit_rfid_tag(id_num):
    session = Session()  # starts the connected session
    type = check_user_level()  # checks the user's type
    if type == 0:  # for type student
        # mapper query to filter by id number and get first result
        req_user = session.query(User.Student).filter_by(id=id_num).first
    else:  # for admin
        # mapper query to filter by id number and get first result
        req_user = session.query(User.Admin).filter_by(id=id_num).first
    while True:  # making an infinite loop
        id, text = reader.read()  # waiting for id to be scanned
        if reader.read():
            id, string = reader.read()  # gets the rfid tag
            req_user.rfid_tag = str(id).strip()  # assigns the tag to the user profile
            session.commit()  # commits the changes
            break  # breaks infinite loop
