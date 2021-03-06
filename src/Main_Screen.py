from tkinter import *
import os
#from mfrc522 import SimpleMFRC522

#reader = SimpleMFRC522()

def delete2():
    screen3.destroy()


def delete4():
    screen1.destroy()


def delete3():
    screen4.destroy()


def delete5():
    dashboard()
    screen6.destroy()


def delete6():
    dashboard()
    screen7.destroy()


def delete7():
    screen1.destroy()


# def card_read():
#     while 1:
#         if reader.read_id():
#             id = reader.read()
#             return str(id).strip()


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
    Button(screen8, text="Click Here to Scan RFID Tag", fg="black", width=30, height=2).grid(row=5, column=3)
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


def Permission():
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


def password_not_recognized():  # Displays message if wrong password is entered
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Password not recognized").pack()
    Button(screen3, text="ok", command=delete2).pack()


def user_not_found():  # Displays message if wrong user name is entered
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="User not found").pack()
    Button(screen4, text="ok", command=delete3).pack()


def login_verify():  # Checks saved information to verify login credentials

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
            print("Login Success")
        else:
            password_not_recognized()
    else:
        user_not_found()


def register():  # screen for user to register their information in order to login
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("User Permissions")
    screen1.geometry("700x400")
    Label(screen1, text="User Permissions").grid(row=0, column=3)
    Label(screen1, text="").grid(row=1)
    global username_verify
    global password_verify

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
    Button(screen1, text="Return", width=10, height=1, command=delete7).grid(row=13)


def login():  # login screen to main window
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Main Screen")
    Label(text="Main Screen", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register User", height="2", width="30", command=register).pack()

    screen.mainloop()


if __name__ == "__main__":
    main_screen()
