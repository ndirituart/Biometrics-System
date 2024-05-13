from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Function that logs in students with constraints of CORRECT Studentname and Admission number
def signIn(user_entry, code_entry):
    Studentname = user_entry.get()
    Admissionnumber = code_entry.get()

    # Control function to login a saved user. This will be removed once we have a database loaded with Student names and admission numbers
    if Studentname == "Patience Njeri" and Admissionnumber == '2077':
        messagebox.showinfo("Success", "Welcome Patience Njeri!")

    elif Studentname != 'Patience Njeri' and Admissionnumber == '2077':
        messagebox.showerror("Invalid", "Invalid Student name and Admission number")

    elif Admissionnumber != '2077':
        messagebox.showerror("Invalid", "Invalid Admission number")

    elif Studentname != "Patience Njeri":
        messagebox.showerror("Invalid", "Invalid Student name")

def Login():
    signIn(user, code)

image = PhotoImage(file='Login.png')
Label(root, image=image, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="light grey")
frame.place(x=480, y=70)

heading = Label(frame, text="Login", bg="light grey", fg="#57a1f8", font=('Microsoft Yattei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e, widget='', end=None):
    widget.delete(0,end)

def on_leave(e, widget=''):
    name = widget.get()
    if name == '':
        widget.insert(0, 'Studentname')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yattei UI Light', 11, "bold"))
user.place(x=30,y=80)
user.insert(0,'Studentname')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=2, bg='white',font=('Microsoft Yattei UI Light',11, "bold"))
code.place(x=30,y=150)
code.insert(0,'Admission number')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)

Button(frame, width=39, pady=7,text='Login', bg='#57a1f8',fg='white',border=0, command=Login).place(x=35,y=204)

root.mainloop()
