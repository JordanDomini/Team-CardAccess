from tkinter import *
import os
import DataLayer as dl
import User
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
id = ""



# all of the "delete" defs below are linked to the return buttons of various windows to allow users
# to backtrack if need be
def delete1():
    screen2.destroy()


def delete2():
    screen3.destroy()


def delete3():
    register_admin_student()
    screen1.destroy()


def delete4():
    screen9.destroy()


def delete5():
    screen10.destroy()


def delete6():
    register_admin_student()
    screen11.destroy()


def delete7():
    screen4.destroy()
    edit_admin_student()


def delete8():
    screen5.destroy()
    edit_admin_student()


def delete9():
    screen6.destroy()
    edit_admin_student()


def delete10():
    screen11.destroy()
    screen7.destroy()

# Used for scanning IDS in the "Register User" window
def register_user_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            if dl.check_lvl(str(id).strip()):
                register_admin_student()
                screen9.destroy()
            else:
                Label(screen3, text="User does not have admin access.", fg="red").grid(row=4, column=4)
            break
    # register_admin_student()
    # screen9.destroy()


# Used for scanning IDs in the "Edit User" window
def edit_user_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            if dl.check_lvl(str(id).strip()):
                admin_enter_id()
                screen3.destroy()
            else:
                Label(screen3, text="User does not have admin access.", fg="red").grid(row=4, column=4)
            break


# Used for scanning IDs in the "admin register" window
def admin_register_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            Label(screen11, text="ID scanned", fg="green").grid(row=6, column=3)
            break


# Used for scanning IDs in the "student permissions" window
def student_permission_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            Label(screen1, text="ID scanned", fg="green").grid(row=6, column=3)
            break


def admin_update(name, id_num):
    global id
    user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=1, active=True)
    admin_usr = User.Admin(Type=1, id=id_num, user=user_usr)
    dl.edit_usr(user_usr, admin_usr)
    screen7.destroy()


def student_update(name, id_num, mach001, mach002, mach003, mach004, mach005, mach006, mach007, mach008, mach009,
                   mach010):
    global id
    user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=0, active=True)
    student_usr = User.Student(Type=0, Mach001=mach001, Mach002=mach002, Mach003=mach003, Mach004=mach004,
                               Mach005=mach005, Mach006=mach006, Mach007=mach007, Mach008=mach008, Mach009=mach009,
                               Mach010=mach010, id=id_num, user=user_usr)
    dl.edit_usr(user_usr, student_usr)
    screen6.destroy()


def admin_get(id_num):
    req_user, req_role = dl.get_usr_by_id(id_num)
    if req_user.Type == 1:
        screen4.destroy()
        admin_edit(req_user, req_role)
    elif req_user.Type == 0:
        screen4.destroy()
        student_edit(req_user, req_role)
    else:
        Label(screen4, text="Not a valid user.", fg="red").grid(row=2, column=3)


def admin_add(name, id_num):
    global id
    if id != "":
        user_usr = dl.get_usr(id)
        if user_usr:
            Label(screen11, text="User already registered.", fg="red").grid(row=6, column=3)
        else:
            delete6()
            user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=1, active=True)
            admin_usr = User.Admin(Type=1, id=id_num, user=user_usr)
            dl.add_usr(user_usr)
            dl.add_usr(admin_usr)
            Label(screen11, text="Admin registered successfully.", fg="green").grid(row=6, column=3)
        id = ""
    else:
        Label(screen11, text="Please scan your ID card!", fg="red").grid(row=6, column=3)


def student_add(name, id_num, mach001, mach002, mach003, mach004, mach005, mach006, mach007, mach008, mach009, mach010):
    global id
    if id != "":
        user_usr = dl.get_usr(id)
        if user_usr:
            Label(screen1, text="User already registered.", fg="red").grid(row=6, column=3)
        else:
            delete3()
            user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=0, active=True)
            student_usr = User.Student(Type=0, Mach001=mach001, Mach002=mach002, Mach003=mach003, Mach004=mach004,
                                       Mach005=mach005, Mach006=mach006, Mach007=mach007, Mach008=mach008,
                                       Mach009=mach009,
                                       Mach010=mach010, id=id_num, user=user_usr)
            dl.add_usr(user_usr)
            dl.add_usr(student_usr)
            Label(screen1, text="Student registered successfully.", fg="green").grid(row=6, column=3)
        id = ""
    else:
        Label(screen1, text="Please scan your ID card!", fg="red").grid(row=6, column=3)


# screen for user to register their information in order to login. This is where the student
# permissions will be allocated
def student_edit(req_user, req_role):
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Edit")
    w, h = 950, 500
    screen6.geometry('%dx%d+%d+%d' % (
    w, h, ((screen6.winfo_screenwidth() / 2) - (w / 2)), ((screen6.winfo_screenheight() / 2) - (h / 2))))
    Label(screen6, text="User Permissions").grid(row=0, column=3)
    Label(screen6, text="").grid(row=1)
    global name_verify
    global ID_verify

    name_verify = StringVar()
    ID_verify = IntVar()
    mach001 = IntVar()
    mach002 = IntVar()
    mach003 = IntVar()
    mach004 = IntVar()
    mach005 = IntVar()
    mach006 = IntVar()
    mach007 = IntVar()
    mach008 = IntVar()
    mach009 = IntVar()
    mach010 = IntVar()
    name_verify.set(req_user.name)
    ID_verify.set(req_user.id)
    mach001.set(req_role.Mach001)
    mach002.set(req_role.Mach002)
    mach003.set(req_role.Mach003)
    mach004.set(req_role.Mach004)
    mach005.set(req_role.Mach005)
    mach006.set(req_role.Mach006)
    mach007.set(req_role.Mach007)
    mach008.set(req_role.Mach008)
    mach009.set(req_role.Mach009)
    mach010.set(req_role.Mach010)

    global name_entry1
    global ID_entry1

    Label(screen6, text="Enter Name").grid(row=2, column=2)
    name_entry1 = Entry(screen6, textvariable=name_verify).grid(row=3, column=2)
    Label(screen6, text="Enter Student ID").grid(row=2, column=4)
    ID_entry1 = Entry(screen6, textvariable=ID_verify, state="disabled").grid(row=3, column=4)
    Label(screen6, text="").grid(row=4)
    Button(screen6, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=student_permission_card_read).grid(row=5, column=3)
    Label(screen6, text="").grid(row=6)
    Label(screen6, text="").grid(row=7)
    but1 = Checkbutton(screen6, text="Machine Name 01", variable=mach001).grid(row=8, column=2)
    but2 = Checkbutton(screen6, text="Machine Name 02", variable=mach002).grid(row=8, column=4)
    Label(screen6, text="").grid(row=9)
    but3 = Checkbutton(screen6, text="Machine Name 03", variable=mach003).grid(row=10, column=2)
    but4 = Checkbutton(screen6, text="Machine Name 04", variable=mach004).grid(row=10, column=4)
    Label(screen6, text="").grid(row=11)
    but5 = Checkbutton(screen6, text="Machine Name 05", variable=mach005).grid(row=12, column=2)
    but6 = Checkbutton(screen6, text="Machine Name 06", variable=mach006).grid(row=12, column=4)
    Label(screen6, text="").grid(row=13)
    but7 = Checkbutton(screen6, text="Machine Name 07", variable=mach007).grid(row=14, column=2)
    but8 = Checkbutton(screen6, text="Machine Name 08", variable=mach008).grid(row=14, column=4)
    Label(screen6, text="").grid(row=15)
    but9 = Checkbutton(screen6, text="Machine Name 09", variable=mach009).grid(row=16, column=2)
    but10 = Checkbutton(screen6, text="Machine Name 10", variable=mach010).grid(row=16, column=4)
    Label(screen6, text="").grid(row=17)
    Button(screen6, text="Return", width=10, height=1, command=delete9).grid(row=18, column=1)
    Button(screen6, text="Enter", width=10, height=2,
           command=lambda: student_add(name_verify.get(), ID_verify.get(), mach001.get(), mach002.get(), mach003.get(),
                                       mach004.get(), mach005.get(), mach006.get(), mach007.get(), mach008.get(),
                                       mach009.get(), mach010.get())).grid(row=18, column=5)
    name_entry1.insert(0, req_user.name)
    ID_entry1.insert(0, req_user.id)
    if req_role.Mach001:
        but1.select()
    elif req_role.Mach002:
        but2.select()
    elif req_role.Mach003:
        but3.select()
    elif req_role.Mach004:
        but4.select()
    elif req_role.Mach005:
        but5.select()
    elif req_role.Mach006:
        but6.select()
    elif req_role.Mach007:
        but7.select()
    elif req_role.Mach008:
        but8.select()
    elif req_role.Mach009:
        but9.select()
    elif req_role.Mach010:
        but10.select()


def admin_edit(req_user, req_role):
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Edit")
    w, h = 900, 300
    screen7.geometry('%dx%d+%d+%d' % (
    w, h, ((screen7.winfo_screenwidth() / 2) - (w / 2)), ((screen7.winfo_screenheight() / 2) - (h / 2))))
    Label(screen7, text="Admin Info").grid(row=0, column=3)
    Label(screen7, text="").grid(row=1)

    name_verify1 = StringVar()
    ID_verify1 = IntVar()
    name_verify1.set(req_user.name)
    ID_verify1.set(req_user.id)

    global name_entry2
    global ID_entry2

    Label(screen7, text="Enter Name").grid(row=2, column=2)
    name_entry2 = Entry(screen7, textvariable=name_verify1).grid(row=3, column=2)
    Label(screen7, text="Enter Admin ID").grid(row=2, column=4)
    ID_entry2 = Entry(screen7, textvariable=ID_verify1, state='disabled').grid(row=3, column=4)
    Label(screen7, text="").grid(row=4)
    Button(screen7, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=admin_register_card_read).grid(row=5, column=3)
    Label(screen7, text="").grid(row=6)
    Label(screen7, text="").grid(row=7)
    Button(screen7, text="Return", width=10, height=1, command=delete10).grid(row=8)
    Button(screen7, text="Enter", width=10, height=2,
           command=lambda: admin_update(name_verify1.get(), ID_verify1.get())).grid(row=8, column=3)
    name_entry2.insert(0, req_user.name)
    ID_entry2.insert(0, req_user.id)


# screen for user to register their information in order to login. This is where the student
# permissions will be allocated
def student_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    w, h = 950, 500
    screen1.geometry('%dx%d+%d+%d' % (
    w, h, ((screen1.winfo_screenwidth() / 2) - (w / 2)), ((screen1.winfo_screenheight() / 2) - (h / 2))))
    Label(screen1, text="User Permissions").grid(row=0, column=3)
    Label(screen1, text="").grid(row=1)
    global name_verify
    global ID_verify

    name_verify = StringVar()
    ID_verify = IntVar()
    mach001 = IntVar()
    mach002 = IntVar()
    mach003 = IntVar()
    mach004 = IntVar()
    mach005 = IntVar()
    mach006 = IntVar()
    mach007 = IntVar()
    mach008 = IntVar()
    mach009 = IntVar()
    mach010 = IntVar()

    global name_entry1
    global ID_entry1

    Label(screen1, text="Enter Name").grid(row=2, column=2)
    name_entry1 = Entry(screen1, textvariable=name_verify).grid(row=3, column=2)
    Label(screen1, text="Enter Student ID").grid(row=2, column=4)
    ID_entry1 = Entry(screen1, textvariable=ID_verify).grid(row=3, column=4)
    Label(screen1, text="").grid(row=4)
    Button(screen1, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=student_permission_card_read).grid(row=5, column=3)
    Label(screen1, text="").grid(row=6)
    Label(screen1, text="").grid(row=7)
    Checkbutton(screen1, text="Machine Name 01", variable=mach001).grid(row=8, column=2)
    Checkbutton(screen1, text="Machine Name 02", variable=mach002).grid(row=8, column=4)
    Label(screen1, text="").grid(row=9)
    Checkbutton(screen1, text="Machine Name 03", variable=mach003).grid(row=10, column=2)
    Checkbutton(screen1, text="Machine Name 04", variable=mach004).grid(row=10, column=4)
    Label(screen1, text="").grid(row=11)
    Checkbutton(screen1, text="Machine Name 05", variable=mach005).grid(row=12, column=2)
    Checkbutton(screen1, text="Machine Name 06", variable=mach006).grid(row=12, column=4)
    Label(screen1, text="").grid(row=13)
    Checkbutton(screen1, text="Machine Name 07", variable=mach007).grid(row=14, column=2)
    Checkbutton(screen1, text="Machine Name 08", variable=mach008).grid(row=14, column=4)
    Label(screen1, text="").grid(row=15)
    Checkbutton(screen1, text="Machine Name 09", variable=mach009).grid(row=16, column=2)
    Checkbutton(screen1, text="Machine Name 10", variable=mach010).grid(row=16, column=4)
    Label(screen1, text="").grid(row=17)
    Button(screen1, text="Return", width=10, height=1, command=delete3).grid(row=18, column=1)
    Button(screen1, text="Enter", width=10, height=2,
           command=lambda: student_add(name_verify.get(), ID_verify.get(), mach001.get(), mach002.get(), mach003.get(),
                                       mach004.get(), mach005.get(), mach006.get(), mach007.get(), mach008.get(),
                                       mach009.get(), mach010.get())).grid(row=18, column=5)


# This is used to close the "Register" window should the user click the "Student" button
def student_reg():
    student_register()
    screen10.destroy()


# Screen for registering admin info
def admin_register():
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Register")
    w, h = 900, 300
    screen11.geometry('%dx%d+%d+%d' % (
    w, h, ((screen11.winfo_screenwidth() / 2) - (w / 2)), ((screen11.winfo_screenheight() / 2) - (h / 2))))
    Label(screen11, text="Admin Info").grid(row=0, column=3)
    Label(screen11, text="").grid(row=1)
    global name_verify1
    global ID_verify1

    name_verify1 = StringVar()
    ID_verify1 = IntVar()

    global name_entry2
    global ID_entry2

    Label(screen11, text="Enter Name").grid(row=2, column=2)
    name_entry2 = Entry(screen11, textvariable=name_verify1).grid(row=3, column=2)
    Label(screen11, text="Enter Admin ID").grid(row=2, column=4)
    ID_entry2 = Entry(screen11, textvariable=ID_verify1).grid(row=3, column=4)
    Label(screen11, text="").grid(row=4)
    Button(screen11, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=admin_register_card_read).grid(row=5, column=3)
    Label(screen11, text="").grid(row=6)
    Label(screen11, text="").grid(row=7)
    Button(screen11, text="Return", width=10, height=1, command=delete6).grid(row=8)
    Button(screen11, text="Enter", width=10, height=2,
           command=lambda: admin_add(name_verify1.get(), ID_verify1.get())).grid(row=8, column=3)


# screen for initial ID scanning for access to the register window
def register_user():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Scan Now")
    w, h = 300, 250
    screen9.geometry('%dx%d+%d+%d' % (
    w, h, ((screen9.winfo_screenwidth() / 2) - (w / 2)), ((screen9.winfo_screenheight() / 2) - (h / 2))))
    Label(screen9, text="").grid(row=0)
    Label(screen9, text="").grid(row=1)
    Label(screen9, text="").grid(row=2)
    Button(screen9, text="Scan ID", width=10, height=2, command=register_user_card_read).grid(row=3, column=4)
    Label(screen9, text="").grid(row=4)
    Label(screen9, text="").grid(row=5)
    Label(screen9, text="").grid(row=6)
    Button(screen9, text="Return", width=5, height=1, command=delete4).grid(row=7)


# screen for deciding which to register, Admin or Student
def register_admin_student():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Which are You Registering?")
    w, h = 350, 350
    screen10.geometry('%dx%d+%d+%d' % (
    w, h, ((screen10.winfo_screenwidth() / 2) - (w / 2)), ((screen10.winfo_screenheight() / 2) - (h / 2))))
    Label(screen10, text="").grid(row=0)
    Label(screen10, text="").grid(row=1)
    Button(screen10, text="Admin", width=20, height=2, command=admin).grid(row=2, column=3)
    Label(screen10, text="").grid(row=3)
    Button(screen10, text="Student", width=20, height=2, command=student_reg).grid(row=4, column=3)
    Label(screen10, text="").grid(row=5)
    Label(screen10, text="").grid(row=6)
    Button(screen10, text="Return", width=5, height=1, command=delete5).grid(row=7)


# window to decide if editing admin or student permissions
def edit_admin_student():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Which are You Editing?")
    w, h = 400, 400
    screen2.geometry('%dx%d+%d+%d' % (
    w, h, ((screen2.winfo_screenwidth() / 2) - (w / 2)), ((screen2.winfo_screenheight() / 2) - (h / 2))))
    Label(screen2, text="").grid(row=0)
    Label(screen2, text="").grid(row=1)
    Button(screen2, text="Admin", width=20, height=2, command=admin_enter_id).grid(row=2, column=3)
    Label(screen2, text="").grid(row=3)
    Button(screen2, text="Student", width=20, height=2, command=student_enter_id).grid(row=4, column=3)
    Label(screen2, text="").grid(row=5)
    Label(screen2, text="").grid(row=6)
    Button(screen2, text="Return", width=5, height=1, command=delete1).grid(row=7)


def admin_enter_id():
    global screen4
    global ID_verify2

    ID_verify2 = IntVar()

    global admin_id
    screen4 = Toplevel(screen)
    screen4.title("Enter ID")
    w, h = 300, 250
    screen4.geometry('%dx%d+%d+%d' % (
    w, h, ((screen4.winfo_screenwidth() / 2) - (w / 2)), ((screen4.winfo_screenheight() / 2) - (h / 2))))
    Label(screen4, text="").grid(row=0)
    Label(screen4, text="").grid(row=1)
    Label(screen4, text="Enter ID").grid(row=2, column=2)
    admin_id = Entry(screen4, textvariable=ID_verify2).grid(row=2, column=3)
    Label(screen4, text="").grid(row=3)
    Label(screen4, text="").grid(row=4)
    Button(screen4, text="Return", width=5, height=1, command=delete7).grid(row=5, column=0)
    Button(screen4, text="Enter", width=5, height=2, command=lambda: admin_get(ID_verify2.get())).grid(row=5, column=3)


def student_enter_id():
    global screen5
    global ID_verify3

    ID_verify3 = 0

    global student_id
    screen5 = Toplevel(screen)
    screen5.title("Enter ID")
    w, h = 300, 250
    screen5.geometry('%dx%d+%d+%d' % (w, h, ((screen5.winfo_screenwidth() / 2) - (w / 2)), ((screen5.winfo_screenheight() / 2) - (h / 2))))
    Label(screen5, text="").grid(row=0)
    Label(screen5, text="").grid(row=1)
    Label(screen5, text="Enter ID").grid(row=2, column=2)
    student_id = Entry(screen5, textvariable=ID_verify3).grid(row=2, column=3)
    Label(screen5, text="").grid(row=3)
    Label(screen5, text="").grid(row=4)
    Button(screen5, text="Return", width=5, height=1, command=delete8).grid(row=5)


# This is used to close the "Register" window should the user click the "Admin" button
def admin():
    admin_register()
    screen10.destroy()


# Screen to accept scanning of ID for access to the next window
def edit_user():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Scan Now")
    w, h = 300, 250
    screen3.geometry('%dx%d+%d+%d' % (
    w, h, ((screen3.winfo_screenwidt3() / 2) - (w / 2)), ((screen3.winfo_screenheight() / 2) - (h / 2))))
    Label(screen3, text="").grid(row=0)
    Label(screen3, text="").grid(row=1)
    Label(screen3, text="").grid(row=2)
    Button(screen3, text="Scan ID", width=10, height=2, command=edit_user_card_read).grid(row=3, column=4)
    Label(screen3, text="").grid(row=4)
    Label(screen3, text="").grid(row=5)
    Label(screen3, text="").grid(row=6)
    Button(screen3, text="Return", width=5, height=1, command=delete2).grid(row=7)


def main_screen():
    global screen
    screen = Tk()
    w, h = 300, 250
    screen.geometry('%dx%d+%d+%d' % (
    w, h, ((screen.winfo_screenwidth() / 2) - (w / 2)), ((screen.winfo_screenheight() / 2) - (h / 2))))
    screen.title("Main Screen")
    Label(text="Main Screen", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Edit User", height="2", width="30", command=edit_user).pack()
    Label(text="").pack()
    Button(text="Register User", height="2", width="30", command=register_user).pack()

    screen.mainloop()


if __name__ == "__main__":
    while 1:
        main_screen()
