from tkinter import *

def clearall():
    principalfield.delete(0, END)
    ratefield.delete(0, END)
    timefield.delete(0, END)
    compoundfield.config(text="")
    principalfield.focus_set()

def calculateci():
    try:
        principal = float(principalfield.get())
        rate = float(ratefield.get())
        time = float(timefield.get())
        
        CI = principal * (pow((1 + rate / 100), time)) - principal
        compoundfield.config(text=f"{CI:.2f}")
    except ValueError:
        compoundfield.config(text="Invalid input")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="lightblue")
    root.geometry("500x250")
    root.title("Compound Interest Calculator")

    label1 = Label(root, text="Principal Amount(Rs): ", fg="white", bg="black")
    label2 = Label(root, text="Rate(%): ", fg="white", bg="black")
    label3 = Label(root, text="Time(years): ", fg="white", bg="black")
    label4 = Label(root, text="Compound Interest: ", fg="white", bg="black")

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    principalfield = Entry(root)
    ratefield = Entry(root)
    timefield = Entry(root)
    compoundfield = Label(root, text="", bg="lightblue", fg="black")

    principalfield.grid(row=1, column=1, padx=10, pady=10)
    ratefield.grid(row=2, column=1, padx=10, pady=10)
    timefield.grid(row=3, column=1, padx=10, pady=10)
    compoundfield.grid(row=5, column=1, padx=10, pady=10)

    button1 = Button(root, text="Clear", command=clearall)
    button2 = Button(root, text="Calculate", command=calculateci)

    button1.grid(row=6, column=0, padx=10, pady=10)
    button2.grid(row=6, column=1, padx=10, pady=10)

    root.mainloop()
