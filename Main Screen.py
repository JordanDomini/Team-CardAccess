from tkinter import *
import os
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def delete1():
    screen2.destroy()


def delete2():
    screen3.destroy()


def delete4():
    register_admin_student()
    screen1.destroy()


def delete3():
    screen3.destroy()


def delete5():
    dashboard()
    screen6.destroy()


def delete6():
    dashboard()
    screen7.destroy()


def delete7():
    screen9.destroy()


def delete8():
    screen10.destroy()


def delete9():
    register_admin_student()
    screen11.destroy()


def card_read():
     while 1:
         if reader.read_id():
             id = reader.read()
             return str(id).strip()


def machineSelection():  # screen to choose machine
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Machine Selection")
    screen6.geometry("800x300")
    Label(screen6, text="Choose a machine").grid(row=0, column=3)
    Button(screen6, text="Machine Name 01", fg="black", width=30, height=2).grid(row=1, column=2)
    Button(screen6, text="Machine Name 02", fg="black", width=30, height=2).grid(row=1, column=4)
    Label(screen6, text="").grid(row=2)
    Button(screen6, text="Machine Name 03", fg="black", width=30, height=2).grid(row=3, column=2)
    Button(screen6, text="Machine Name 04", fg="black", width=30, height=2).grid(row=3, column=4)
    Label(screen6, text="").grid(row=4)
    Button(screen6, text="Machine Name 05", fg="black", width=30, height=2).grid(row=5, column=2)
    Button(screen6, text="Machine Name 06", fg="black", width=30, height=2).grid(row=5, column=4)
    Label(screen6, text="").grid(row=6)
    Button(screen6, text="Return", width=10, height=1, command=delete5).grid(row=7)


def chooseMachine():
    machineSelection()
    screen5.destroy()


def editMachine():  # Screen to allow edits to made to machine information
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Edit Machine")
    screen7.geometry("300x250")
    Label(screen7, text="Machine details").pack()
    Label(screen7, text="").pack()
    Label(screen7, text="Machine Name").pack()
    Label(screen7, text="Enter Machine name").pack()
    Label(screen7, text="").pack()
    Label(screen7, text="Machine description").pack()
    Label(screen7, text="Enter machine description").pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Return", width=10, height=1, command=delete6).pack(side=LEFT)


def edit():
    editMachine()
    screen5.destroy()


def userPermission():  # Screen for giving the users permission
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("User Permissions")
    screen8.geometry("700x400")
    Label(screen8, text="User Permissions").grid(row=0, column=3)
    Label(screen8, text="").grid(row=1)
    global username_verify
    global password_verify

    name_verify = StringVar()
    ID_verify = IntVar()

    global name_entry1
    global ID_entry1

    Label(screen8, text="Enter Name").grid(row=2, column=2)
    name_entry1 = Entry(screen8, textvariable=name_verify).grid(row=3, column=2)
    Label(screen8, text="Enter Student ID").grid(row=2, column=4)
    ID_entry1 = Entry(screen8, textvariable=ID_verify).grid(row=3, column=4)
    Label(screen8, text="").grid(row=4)
    Button(screen8, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2, command=card_read).grid(row=5, column=3)
    Label(screen8, text="").grid(row=6)
    Checkbutton(screen8, text="Machine Name 01").grid(row=7, column=2)
    Checkbutton(screen8, text="Machine Name 02").grid(row=7, column=4)
    Label(screen8, text="").grid(row=8)
    Checkbutton(screen8, text="Machine Name 03").grid(row=9, column=2)
    Checkbutton(screen8, text="Machine Name 04").grid(row=9, column=4)
    Label(screen8, text="").grid(row=10)
    Checkbutton(screen8, text="Machine Name 05").grid(row=11, column=2)
    Checkbutton(screen8, text="Machine Name 06").grid(row=11, column=4)
    Label(screen8, text="").grid(row=12)
    Button(screen8, text="Return", width=10, height=1, command=delete7).grid(row=13)


def permission():
    userPermission()
    screen5.destroy()


def dashboard():  # Main screen after login, different options for user functionality
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Dashboard")
    screen5.geometry("400x300")
    Label(screen5, text="Dashboard").pack()
    Button(screen5, text="User Permissions", fg="black", width=30, height=2, command=Permission).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Add a machine", fg="black", width=30, height=2).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Edit a Machine", fg="black", width=30, height=2, command=edit).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Choose a machine", fg="black", width=30, height=2, command=chooseMachine).pack()
    Label(screen5, text="").pack()


def login_success():
    dashboard()
    screen2.destroy()


def student_permission():  # screen for user to register their information in order to login
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("700x400")
    Label(screen1, text="User Permissions").grid(row=0, column=3)
    Label(screen1, text="").grid(row=1)
    global name_verify
    global ID_verify

    name_verify = StringVar()
    ID_verify = IntVar()

    global name_entry1
    global ID_entry1

    Label(screen1, text="Enter Name").grid(row=2, column=2)
    name_entry1 = Entry(screen1, textvariable=name_verify).grid(row=3, column=2)
    Label(screen1, text="Enter Student ID").grid(row=2, column=4)
    ID_entry1 = Entry(screen1, textvariable=ID_verify).grid(row=3, column=4)
    Label(screen1, text="").grid(row=4)
    Button(screen1, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2, command=card_read).grid(row=5, column=3)
    Label(screen1, text="").grid(row=6)
    Checkbutton(screen1, text="Machine Name 01").grid(row=7, column=2)
    Checkbutton(screen1, text="Machine Name 02").grid(row=7, column=4)
    Label(screen1, text="").grid(row=8)
    Checkbutton(screen1, text="Machine Name 03").grid(row=9, column=2)
    Checkbutton(screen1, text="Machine Name 04").grid(row=9, column=4)
    Label(screen1, text="").grid(row=10)
    Checkbutton(screen1, text="Machine Name 05").grid(row=11, column=2)
    Checkbutton(screen1, text="Machine Name 06").grid(row=11, column=4)
    Label(screen1, text="").grid(row=12)
    Button(screen1, text="Return", width=10, height=1, command=delete4).grid(row=13)


def student():
    student_permission()
    screen10.destroy()


def admin_register():  # screen for registering admin info
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Register")
    screen11.geometry("700x400")
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
    Button(screen11, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2, command=card_read).grid(row=5, column=3)
    Label(screen11, text="").grid(row=6)
    Button(screen11, text="Return", width=10, height=1, command=delete9).grid(row=7)


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
    Button(screen9, text="Scan ID", width=10, height=2, command=card_read).grid(row=3, column=4)
    Label(screen9, text="").grid(row=4)
    Label(screen9, text="").grid(row=5)
    Label(screen9, text="").grid(row=6)
    Button(screen9, text="Return", width=5, height=1, command=delete7).grid(row=7)


def register_scan():
    register_admin_student()
    screen9.destroy()


def edit_scan():
    edit_admin_student()
    screen3.destroy()


def register_admin_student():  # screen for deciding which to register, Admin or Student
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Which are You?")
    screen10.geometry("400x400")
    Label(screen10, text="").grid(row=0)
    Label(screen10, text="").grid(row=1)
    Button(screen10, text="Admin", width=20, height=2, command=admin).grid(row=2, column=3)
    Label(screen10, text="").grid(row=3)
    Button(screen10, text="Student", width=20, height=2, command=student).grid(row=4, column=3)
    Label(screen10, text="").grid(row=5)
    Label(screen10, text="").grid(row=6)
    Button(screen10, text="Return", width=5, height=1, command=delete8).grid(row=7)


def edit_admin_student():  # login screen to main window
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Which are You?")
    screen2.geometry("400x400")
    Label(screen2, text="").grid(row=0)
    Label(screen2, text="").grid(row=1)
    Button(screen2, text="Admin", width=20, height=2, command=admin).grid(row=2, column=3)
    Label(screen2, text="").grid(row=3)
    Button(screen2, text="Student", width=20, height=2, command=student).grid(row=4, column=3)
    Label(screen2, text="").grid(row=5)
    Label(screen2, text="").grid(row=6)
    Button(screen2, text="Return", width=5, height=1, command=delete1).grid(row=7)


def edit_user():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Scan Now")
    screen3.geometry("300x250")
    Label(screen3, text="").grid(row=0)
    Label(screen3, text="").grid(row=1)
    Label(screen3, text="").grid(row=2)
    Button(screen3, text="Scan ID", width=10, height=2, command=card_read).grid(row=3, column=4)
    Label(screen3, text="").grid(row=4)
    Label(screen3, text="").grid(row=5)
    Label(screen3, text="").grid(row=6)
    Button(screen3, text="Return", width=5, height=1, command=delete3).grid(row=7)


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
