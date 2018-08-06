
import time
import classes.Methods as met
import tkinter as tk
from tkinter import *  # ttk, PhotoImage, Label, Menu, Canvas
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from tkinter import ttk

# ------------------------------------------------------------------------------
# GLOBALS
# ------------------------------------------------------------------------------
icon_path = 'icono.ico'
imref_path = '000012.jpg'
iminput_path = '000013.jpg'


# ------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------
def quit():
    root.quit()
    root.destroy()
    exit()


def do_match():
    global imref_path, iminput_path, process_frame

    progress_bar = ttk.Progressbar(process_frame, orient='horizontal', length=300, mode='determinate')
    progress_bar.grid(row=1, columnspan=6)

    images_matched = met.match(met.resource_path(imref_path), met.resource_path(iminput_path))

    Image_matched = Image.fromarray(images_matched)
    Image_matched.thumbnail((400, 400), Image.ANTIALIAS)
    Image_matched = ImageTk.PhotoImage(Image_matched)

    match_Label = Label(process_frame, image=Image_matched, compound=tk.CENTER, width=400, height=200)
    match_Label.grid(row=1, columnspan=6)
    match_Label.image = Image_matched


# Create instance
root = tk.Tk()

# Add title
root.title("REGIM")
root.geometry("800x550+0+0")

# Change icon
root.iconbitmap(met.resource_path(icon_path))

# Disable resizing the GUI
root.resizable(False, False)

# Add canvas
canvas = Canvas(root, width=100, height=100)
# canvas.pack()

# Creating menu bar
menuBar = Menu(root)
root.config(menu=menuBar)

# Create menu and add menu items
file_menu = Menu(menuBar, tearoff=0)
file_menu.add_command(label="Load", command="")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

menuBar.add_cascade(label="File", menu=file_menu)

# Add another menu
help_menu = Menu(menuBar, tearoff=0)
help_menu.add_command(label="About")

menuBar.add_cascade(label="Help", menu=help_menu)

# Create a container to hold widgets
menu_frame = LabelFrame(root, text="", background="white", width=100, height=550).grid(column=0, row=0, rowspan=4,
                                                                                       padx=0, pady=0)
process_frame = LabelFrame(root, text="", background="gray", width=700, height=550).grid(column=1, row=0, rowspan=2,
                                                                                       padx=0, pady=0, columnspan=2)

# Adding labels

match_button = Button(menu_frame, text="Match features", command=do_match,
                      background="#ff6464", width=12).grid(column=0, row=0)

# Adding images
size = 200, 200
im_reference = Image.open(met.resource_path(imref_path))
im_reference.thumbnail(size, Image.ANTIALIAS)
im_reference = ImageTk.PhotoImage(im_reference)

im_input = Image.open(met.resource_path(iminput_path))
im_input.thumbnail(size, Image.ANTIALIAS)
im_input = ImageTk.PhotoImage(im_input)

ref_Label = Label(process_frame, image=im_reference, text="", compound=tk.CENTER)
ref_Label.grid(row=0, column=1)

input_Label = Label(process_frame, image=im_input, text="", compound=tk.CENTER, width=200, height=200)
input_Label.grid(row=0, column=2)

match_Label = Label(process_frame, image=None, text="", compound=tk.CENTER, width=57, height=14)
match_Label.grid(row=1, columnspan=6)

root.mainloop()
