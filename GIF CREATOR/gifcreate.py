from tkinter import *
from tkinter import messagebox, filedialog
import imageio

# Function to convert Image to GIF
def convertToGIF():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpeg;*.jpg")])
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    try:
        # Reading the selected image
        img = imageio.imread(file_path)

        # Creating a GIF with a single image (the same image looped)
        gif_path = file_path.rsplit('.', 1)[0] + ".gif"
        imageio.mimsave(gif_path, [img] * 10, duration=5)  # Loop the image multiple times to create a GIF effect

        messagebox.showinfo("GIF Creator", f"GIF saved successfully as {gif_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while creating the GIF:\n{str(e)}")

# Creating the window
wn = Tk()
wn.title("GIF Creator")
wn.geometry('500x300')
wn.config(bg='azure')

# The main label
Label(wn, text='GIF Creator', bg='azure', fg='black', font=('Times', 20, 'bold')).place(x=160, y=10)

# Instruction label
Label(wn, text='Click the button to select an image file to convert into GIF', bg='azure2', anchor="e", justify=LEFT).place(x=20, y=100)

# Button to select image and convert it to GIF
Button(wn, text="Select Image and Convert", bg='ivory3', font=('calibre', 13), command=convertToGIF).place(x=150, y=150)

# Runs the window till it is closed by the user
wn.mainloop()