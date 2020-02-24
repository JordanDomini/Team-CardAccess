from tkinter import *
import os
import DataLayer as dl
import User
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
id = ""


def delete1():
    screen2.destroy()
    main_screen()


def delete2():
    screen3.destroy()
    main_screen()


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


def register_user_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            register_admin_student()
            screen9.destroy()
            break


def edit_user_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            edit_admin_student()
            screen3.destroy()
            break


def admin_register_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            Label(screen11, text="ID scanned", fg="green").grid(row=6, column=3)
            break


def student_permission_card_read():
    global id
    while 1:
        if reader.read():
            id, string = reader.read()
            print(str(id).strip())
            Label(screen1, text="ID scanned", fg="green").grid(row=6, column=3)
            break


def admin_add(name, id_num):
    global id
    if id != "":
        delete6()
        user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=1, active=True)
        admin_usr = User.Admin(Type=1, id=id_num)
        dl.add_usr(user_usr)
        dl.add_usr(admin_usr)
        id = ""
        Label(screen10, text="Admin registered successfully.", fg="green").grid(row=6, column=3)
    else:
        Label(screen11, text="Please scan your ID card!", fg="red").grid(row=6, column=3)


def student_add(name, id_num, mach001, mach002, mach003, mach004, mach005, mach006, mach007, mach008, mach009, mach010):
    global id
    if id != "":
        delete3()
        user_usr = User.User(id=id_num, name=name, rfid_tag=id, Type=0, active=True)
        student_usr = User.Student(Type=0, Mach001=mach001, Mach002=mach002, Mach003=mach003, Mach004=mach004,
                                   Mach005=mach005, Mach006=mach006, Mach007=mach007, Mach008=mach008, Mach009=mach009,
                                   Mach010=mach010, id=id_num)
        dl.add_usr(user_usr)
        dl.add_usr(student_usr)
        id = ""
        Label(screen10, text="Student registered successfully.", fg="green").grid(row=6, column=3)
    else:
        Label(screen1, text="Please scan your ID card!", fg="red").grid(row=6, column=3)


def student_register():  # screen for user to register their information in order to login
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("1000x600")
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
                                       mach009.get(),
                                       mach010.get())).grid(row=18, column=5)


def student_reg():
    student_register()
    screen10.destroy()


def admin_register():  # screen for registering admin info
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Register")
    screen11.geometry("900x400")
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


def admin():
    admin_register()
    screen10.destroy()


def register_user():  # screen for initial RFID scanning
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Scan Now")
    screen9.geometry("300x250")
    Label(screen9, text="").grid(row=0)
    Label(screen9, text="").grid(row=1)
    Label(screen9, text="").grid(row=2)
    Button(screen9, text="Scan ID", width=10, height=2, command=register_user_card_read).grid(row=3, column=4)
    Label(screen9, text="").grid(row=4)
    Label(screen9, text="").grid(row=5)
    Label(screen9, text="").grid(row=6)
    Button(screen9, text="Return", width=5, height=1, command=delete4).grid(row=7)


def register_admin_student():  # screen for deciding which to register, Admin or Student
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Which are You Registering?")
    screen10.geometry("400x400")
    Label(screen10, text="").grid(row=0)
    Label(screen10, text="").grid(row=1)
    Button(screen10, text="Admin", width=20, height=2, command=admin).grid(row=2, column=3)
    Label(screen10, text="").grid(row=3)
    Button(screen10, text="Student", width=20, height=2, command=student_reg).grid(row=4, column=3)
    Label(screen10, text="").grid(row=5)
    Label(screen10, text="").grid(row=6)
    Button(screen10, text="Return", width=5, height=1, command=delete5).grid(row=7)


def edit_admin_student():  # decide if editing admin or student permissions
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Which are You Editing?")
    screen2.geometry("400x400")
    Label(screen2, text="").grid(row=0)
    Label(screen2, text="").grid(row=1)
    Button(screen2, text="Admin", width=20, height=2, command=admin).grid(row=2, column=3)
    Label(screen2, text="").grid(row=3)
    Button(screen2, text="Student", width=20, height=2, command=student_reg).grid(row=4, column=3)
    Label(screen2, text="").grid(row=5)
    Label(screen2, text="").grid(row=6)
    Button(screen2, text="Return", width=5, height=1, command=delete1).grid(row=7)


def edit_user():  # Screen to accept scanning of ID
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Scan Now")
    screen3.geometry("300x250")
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
    screen.geometry("300x250")
    screen.title("Main Screen")
    Label(text="Main Screen", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Edit User", height="2", width="30", command=edit_user).pack()
    Label(text="").pack()
    Button(text="Register User", height="2", width="30", command=register_user).pack()

    screen.mainloop()


if __name__ == "__main__":
    main_screen()
