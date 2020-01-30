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
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@10.0.0.1/test_db'.format(USR, PWD)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

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

def check_user_level(scanned_tag):
    session = Session()
    req_user = session.query(User).filter_by(rfid_tag=scanned_tag).first
    return req_user.Type

def get_user(scanned_tag):
    session = Session()
    type = check_user_level(scanned_tag)
    if type == 0:
        req_user = session.query(Student)

def addUser(user_info):
    session = Session()
    session.add(user_info)
    session.commit()
    return True

def edit_rfid_tag(id_num):
    session = Session()
    type = check_user_level()
    if type == 0:
        req_user = session.query(Student).filter_by(id=id_num).first
    else:
        req_user = session.query(Admin).filter_by(id=id_num).first
    try:
        while True:  # making an infinite loop
            id, text = reader.read()  # waiting for id to be scanned
            while time.monotonic() < future:
                if reader.read():
                    if time.monotonic() < future:
                        id, string = reader.read()
                        break
                    else:
                        future = time.monotonic() + 1
                req_user.rfid_tag = str(id).strip()
                session.commit()
    except:
        GPIO.cleanup()