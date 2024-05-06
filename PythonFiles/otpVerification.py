#This file does On The Phone verification for users to get verified
from idlelib import window

import cv2
import self
from twilio.rest import Client
from tkinter import *
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import smtplib
import random
import time
from PIL import Image, ImageTk

class otpVerification:
    def __init__(self, window):
        #takes window to display all attributes and mothods for this class
       self.window = window
       self.window.geometry ("1366x720+0+0")
       self.window.title ("Account Verification Page")
       self.window.resizable (False, False)
       self.start()

# Create the Tkinter window
root = Tk()
app = otpVerification(root)
root.mainloop()

def start(self):
      #starts the verification process
    self.login_frame = PhotoImage(file="C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/uiBackground/otp_verification_frame.jpeg")
    self.image_panel = Label(self.window,image=self.login_frame)
    self.image_panel.pack(fill = 'both', expand='yes')
    self.txt = "Account Verification"
    self.count = 0
    self.text = ''
    self.color= ["#000000"]
    self.heading = Label(self.window, text=self.txt, font=('yu gothic ui'), size=(12), weight = ('bold'), relief = FLAT)
    self.heading.place (relx=470, rely=70, width=450 , height=450)

     #======================== email =======================
    self.email_label= Label(self.window, text= "Email or phone number", font=('yu gothic'),size=(12), weight = ('bold'),)
    self.email_label.place (relx=495, rely=180)
    self.email_entry = Entry(self.window,font=(('yu gothic'),12))
    self.email_entry.place (relx=530, rely=210, width=380)

    #========================OTP==========================
    self.otp_label = Label(self.window, text="Recent OTP", font=('yu gothic'), size=(12),weight=('bold'), )
    self.otp_label.place(relx=495, rely=295)
    self.otp_entry = Entry(self.window, font=(('yu gothic'), 12))
    self.otp_entry.place(relx=350, rely=325, width=380)

      # ========================Verify Button==========================
    self.verify= PhotoImage(file='C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/uiBackground/verify_button.jpeg')
    self.verify_button = Button(self.window, image =self.verify, cursor="hand2", command= self.click_verification)
    self.verify_button.place(relx=640, rely= 403)

    # ========================Submit Button==========================
    self.send_otp = PhotoImage(file='C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/uiBackground/send_otp.jpeg')
    self.send_otp_button = Button(self.window, image=self.verify, cursor="hand2", command=self.click_validation)
    self.verify_button.place(relx=500, rely=503)

    # ========================Exit Button==========================
    self.exit_img = PhotoImage(file='C:/Users/Pashie/PycharmProjects/pythonProject/AuthenticationSystem/uiBackground/exit.jpeg')
    self.verify_button = Button(self.window, image=self.verify, cursor="hand2", command=self.click_exit)
    self.verify_button.place(relx=783, rely=503)

   # ========================Timer Button==========================
    self.timer_label = Label(self.window, text='Countdown', font="yu gothic", size=13, weight="bold")
    self.timer_label.place (relx=670, rely=590)

    self.sec = StringVar()
    self.sec_entry = Entry(self.window,  textvariable=self.sec,width=2, font="yu gothic ui semibold", size=12)
    self.sec_entry.place(relx=725, rely=550)
    self.sec.sets('00')

    self.mins= StringVar()
    self.mins_Entry = Entry(self.window, textvariable=self.mins, width=2, font="yu gothic ui semibold", size=12)
    self.mins_Entry.place(relx=700, rely=550)
    self.mins.set('02')

    self.hs = StringVar()
    self.hrs_Entry = Entry(self.window, textvariable=self.hs, width=2, font="yu gothic ui semibold", size=12)
    self.hrs_Entry.place(relx=675, rely=550)
    self.hrs.set('00')


def validation (self):
#validates if email entry field is left empty and gives feedback
if self.email_entry.get()=='':
    messagebox.showinfo("Empty","Please enter your email address or mobile number")
else:
    self.click_send_otp()

def countdown(self):
    times = int (self.hrs.get())*3600 + int(self.mins.get()*60 + int(self.sec.get()))
    while times >-1:
        minute, second = (times//60, times%60)
        hour = 0
        if minute>60:
            hour, minute = (minute//60, minute%60)
        self.sec.set(second)
        self.mins.set(minute)
        self.hrs.set(hour)

        self.window.update()
        time.sleep(1)
        if (times == 0):
            messagebox.showinfo("Time's up","You must resend the otp code")
        self.sec.set('00')
        self.mins.set('02')
        self.hrs.set('00')
    times -=1










