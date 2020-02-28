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
IP = '10.250.250.250'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/test_db'.format(USR, PWD, IP)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
fo.close()
session = Session()


# checks permissions of student or just if admin
def check_user_permission(scanned_tag):
    req_user = session.query(User.User).filter_by(rfid_tag=scanned_tag).first()
    if req_user:
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
    req_user = session.query(User.User).filter_by(rfid_tag=scanned_tag).first()
    if req_user:
        if req_user.Type == 1:
            return True
        else:
            return False
    else:
        return False


# gets user
def get_user(scanned_tag):
    return session.query(User.User).filter_by(rfid_tag=scanned_tag).first()


# adds user to db using an existing object
def addUser(user_info):
    session.add(user_info)
    session.commit()
    return True


# edit the rfid tag of an existing user
def edit_user(user_user, user_role):
    req_user = session.query(User.User).filter_by(id=user_user.id).first()
    if req_user.Type == 0:  # for type student
        # mapper query to filter by id number and get first result
        req_role = session.query(User.Student).filter_by(id=user_user.id).first()
        req_role.Mach001 = user_role.Mach001
        req_role.Mach002 = user_role.Mach002
        req_role.Mach003 = user_role.Mach003
        req_role.Mach004 = user_role.Mach004
        req_role.Mach005 = user_role.Mach005
        req_role.Mach006 = user_role.Mach006
        req_role.Mach007 = user_role.Mach007
        req_role.Mach008 = user_role.Mach008
        req_role.Mach009 = user_role.Mach009
        req_role.Mach0010 = user_role.Mach0010
    elif req_user.Type == 1:
        req_role = session.query(User.Admin).filter_by(id=user_user.id).first()
    req_user.name = user_user.name
    if user_user.rfid_tag != "":
        req_user.rfid_tag = user_user.rfid_tag
    req_user.active = user_user.active
    session.flush()
    session.commit()


def get_user_by_id(id_no):
    req_user = session.query(User.User).filter_by(id=id_no).first()
    if req_user.Type == 0:
        req_role = session.query(User.Student).filter_by(id=id_no).first()
    elif req_user.Type == 1:
        req_role = session.query(User.Admin).filter_by(id=id_no).first()
    else:
        req_role = None
    return  req_user, req_role