from tkinter import Label, Tk
import time 

app_window = Tk()
app_window.title("Digital Clock")

text_font= ("SF Pro Display Heavy", 69, 'bold')
background = "#0a0f0d"
foreground= "#fff"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digitalclock():
    timelive = time .strftime("%H:%M:%S")
    label.config(text=timelive)
    label.after(200, digitalclock)
    
digitalclock()
app_window.mainloop()