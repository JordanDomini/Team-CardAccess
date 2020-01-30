from tkinter import *
import os


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


def machineSelection():  # screen to choose machine
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Machine Selection")
    screen6.title("800x800")
    Label(screen6, text="Choose a machine").pack()
    Button(screen6, text="Machine Name 01", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Machine Name 02", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Machine Name 03", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Machine Name 04", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Machine Name 05", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Machine Name 06", fg="black", width=30, height=2).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Return", width=10, height=1, command=delete5).pack()
    Label(screen6, text="").pack()


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


def chooseMachine():
    machineSelection()
    screen5.destroy()


def dashboard():  # Main screen after login, different options for user functionality
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Dashboard")
    screen5.title("800x800")
    Label(screen5, text="Dashboard").pack()
    Button(screen5, text="Add a New User", fg="black", width=30, height=2).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Edit User Permissions", fg="black", width=30, height=2).pack()
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


def register_user():  # Saves new user name and password for future login attempts

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successful", fg="green", font=("calibri", 11)).pack()


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
    screen1.title("Register User")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    global username_entry
    global password_entry
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, comman=register_user).pack()
    Button(screen1, text="Return", width=10, height=1, command=delete4).pack()


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


main_screen()
