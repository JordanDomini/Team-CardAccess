from tkinter import *
import os
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


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
     while 1:
         if reader.read_id():
             id = reader.read()
             print(str(id).strip())
             register_admin_student()
             screen9.destroy()
             break


def edit_user_card_read():
    while 1:
        if reader.read_id():
            id1 = reader.read()
            print(str(id).strip())
            edit_admin_student()
            screen3.destroy()
            break


def admin_register_card_reader():
    while 1:
        if reader.read.id():
            id2 = reader.read()
            print(str(id).strip())
            admin_register()
            screen11.destroy()
            break


def student_permission_card_read():
    while 1:
        if reader.read.id():
            id3 = reader.read()
            print(str(id).strip())
            student_permission()
            screen1.destroy()
            break


def student_register():  # screen for user to register their information in order to login
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
    Button(screen1, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=student_permission_card_read).grid(row=5, column=3)
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
    Button(screen1, text="Return", width=10, height=1, command=delete3).grid(row=13)


def student():
    student_register()
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
    Button(screen11, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2,
           command=admin_register_card_read).grid(row=5, column=3)
    Label(screen11, text="").grid(row=6)
    Button(screen11, text="Return", width=10, height=1, command=delete6).grid(row=7)


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
    Button(screen10, text="Student", width=20, height=2, command=student).grid(row=4, column=3)
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
    Button(screen2, text="Student", width=20, height=2, command=student).grid(row=4, column=3)
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
