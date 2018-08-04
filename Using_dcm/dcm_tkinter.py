import pydicom
import tkinter as tk
from tkinter import *  # ttk, PhotoImage, Label
from PIL import Image, ImageTk

# Create instance
win = tk.Tk()

# Add title
win.title("Files .dcm")
win.geometry("850x550+0+0")


# Disable resizing the GUI
win.resizable(False, False)
canvas = Canvas(win, width=100, height=100)

dcm_read = pydicom.dcmread("images/test0.dcm")  # change the path

# I just had to print this Ima.pixel_array out to show you the lists
dcm_array = dcm_read.pixel_array

dcm_file = Image.fromarray(dcm_array)
# dcm_file.show()
# print(dcm_file)

# bitmap = ImageTk.PhotoImage(dcm_file)

dcm_image = ImageTk.PhotoImage(dcm_file)
yena = ImageTk.PhotoImage(Image.open("images/yena.jpg"))

# Add label
myLabel = Label(win, image=dcm_image, text="", compound=tk.CENTER, width=450, height=450)
myLabel.grid(column=0, columnspan=3)
# myLabel.place(width=450, height=450)
myLabel.configure(background="#c56a87")

win.mainloop()

