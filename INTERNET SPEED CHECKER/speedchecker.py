from tkinter import *
from tkinter import messagebox
import pyspeedtest


def checkspeed():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+ " Bytes per second")
    messagebox.showinfo("Download Speed", a1)
    
root = Tk()
root.title("INTERNET SPEED CHECKER")
root.geometry("700x500")
root.configure(bg="black")

label1 = Label(root, text="Internet Speed Checker", font=("SF Pro", 20), bg="black", fg="white")
button1 = Button(root, text="CHECK SPEED", font=("SF Pro", 15), bg="white", fg="black", command=checkspeed)

label1.pack(pady=20)
button1.pack(pady=20)

root.mainloop()
