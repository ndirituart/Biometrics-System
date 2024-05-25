from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

root = Tk()
root.title("Student Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Function that logs in students with constraints of CORRECT Studentname and Admission number
def login(student_name, admission_number):
    # Database configuration
    config = {
        'user': 'madedech',
        'password': 'S@w@s@w@45!',
        'host': 'localhost',
        'database': 'madedech_university_portal'
    }

    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute SQL query to verify user credentials
        query = "SELECT * FROM student_login WHERE student_names = %s AND Admission_number = %s"
        cursor.execute(query, (student_name, admission_number))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", f"Welcome {student_name}!")
        else:
            messagebox.showerror("Invalid", "Invalid Student name or Admission number")

    except Error as error:
        print(f"Error: {error}")
        messagebox.showerror("Database Error", "An error occurred while connecting to the database")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# Function to be called when the login button is pressed
def perform_login():
    user_value = user.get()
    code_value = code.get()
    Login(user_value, code_value)

# Original Login function which calls the login function
def Login(user, code):
    login(user, code)

image = PhotoImage(file='Login.png')
Label(root, image=image, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="light grey")
frame.place(x=480, y=70)

heading = Label(frame, text="Login", bg="light grey", fg="#57a1f8", font=('Microsoft Yattei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e, widget, placeholder):
    widget.delete(0, END)
    widget.config(fg='black')

def on_leave(e, widget, placeholder):
    if widget.get() == '':
        widget.insert(0, placeholder)
        widget.config(fg='grey')

user_placeholder = 'Studentname'
user = Entry(frame, width=25, fg='grey', border=0, bg="white", font=('Microsoft Yattei UI Light', 11, "bold"))
user.place(x=30, y=80)
user.insert(0, user_placeholder)
user.bind('<FocusIn>', lambda event: on_enter(event, user, user_placeholder))
user.bind('<FocusOut>', lambda event: on_leave(event, user, user_placeholder))

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

code_placeholder = 'Admission number'
code = Entry(frame, width=25, fg='grey', border=2, bg='white', font=('Microsoft Yattei UI Light', 11, "bold"))
code.place(x=30, y=150)
code.insert(0, code_placeholder)
code.bind('<FocusIn>', lambda event: on_enter(event, code, code_placeholder))
code.bind('<FocusOut>', lambda event: on_leave(event, code, code_placeholder))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Login', bg='#57a1f8', fg='white', border=0, command=perform_login).place(x=35, y=204)

root.mainloop()
