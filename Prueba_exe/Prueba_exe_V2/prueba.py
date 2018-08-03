# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
import tkinter as tk
from tkinter import *  # ttk, PhotoImage, Label
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

import classes.myClasses as myf




# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -----------------------------------------------------------------------------
# METHODS
# -----------------------------------------------------------------------------
def quit():
    win.quit()
    win.destroy()
    exit()

def openFile():
    global path, size
    path = askopenfilename(initialdir=".",
                                filetypes =(("Image File .jpg", "*.jpg"),("All Files","*.*")),
                                title = "Choose an imgage."
                           )
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        size = 450, 450
        global label_image, myLabel
        label_image = Image.open(path)
        label_image.thumbnail(size, Image.ANTIALIAS)
        myLabel.config(width=450, height=450)
        tkImage = ImageTk.PhotoImage(label_image)
        myLabel.config(image=tkImage, text="")
        myLabel.image = tkImage


    except:
        print("No file exists")


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# GLOBALS
path = None
my_logo = "regim_logo.ico"
back_image = "yena.jpg"
# -----------------------------------------------------------------------------
# Create instance
win = tk.Tk()

# Add title
win.title("REGIM")
win.geometry("450x570+0+0")

# Change icon
win.iconbitmap(myf.resource_path(my_logo))

# Disable resizing the GUI
win.resizable(False, False)

# Adding a label
# ttk.Label(win, text="Running...").grid(column=3, row=3)

# Add canvas
canvas = Canvas(win, width=100, height=100)
#canvas.pack()


# #Add image
# ruta = "images/yena.jpg"
# my_image = Image.open(ruta)
#
# #B&W image
# #met.blanco_negro(my_image)
#
# #BgImage = PhotoImage(file= ruta)
# BgImage = ImageTk.PhotoImage(my_image)
size = 450, 450
test_image = Image.open(myf.resource_path(back_image))
test_image.thumbnail(size, Image.ANTIALIAS)
test_image2 = ImageTk.PhotoImage(test_image)

myLabel = Label(win, image=test_image2, text="Load image.jpg", compound=tk.CENTER, width=450, height=450, font=("Verdana", 30))
myLabel.grid(column=0, columnspan= 2)
#myLabel.place(width=450, height=450)
myLabel.configure(background="#c56a87")
label_image = None



# Creating menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Create menu and add menu items
file_menu = Menu(menuBar, tearoff=0)
file_menu.add_command(label="Load image", command=openFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

menuBar.add_cascade(label="File", menu=file_menu)

# Add another menu
help_menu = Menu(menuBar, tearoff=0)
help_menu.add_command(label="About")

menuBar.add_cascade(label="Help", menu=help_menu)

# Add radiobuttons
# Radiobutton globals
color1 = "Red"
color2 = "Blue"


# Radiobutton callback
def radCall():
    try:
        rad_image = Image.open(path)
        rad_image.thumbnail(size, Image.ANTIALIAS)
        radSel = radVar.get()
        if radSel == 1:
            rad_BgImage = ImageTk.PhotoImage(rad_image)
            myLabel.configure(image=rad_BgImage)
            myLabel.image = rad_BgImage
            #win.configure(background= color1)
        elif radSel == 2:
            rad_BgImage = ImageTk.PhotoImage(myf.blanco_negro(rad_image))
            myLabel.configure(image=rad_BgImage)
            myLabel.image = rad_BgImage
            #win.configure(background= color2)
        elif radSel == 3:
            rad_BgImage = ImageTk.PhotoImage(myf.escala_de_grises(rad_image))
            myLabel.configure(image=rad_BgImage)
            myLabel.image = rad_BgImage
        elif radSel == 4:
            rad_BgImage = ImageTk.PhotoImage(myf.negativo_color(rad_image))
            myLabel.configure(image=rad_BgImage)
            myLabel.image = rad_BgImage
    except:
        pass


# Create 2 radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text="Color", variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=1, sticky=tk.W, columnspan=1)

rad2 = tk.Radiobutton(win, text="Black&White", variable=radVar, value=2, command=radCall)
rad2.grid(column=0, row=2, sticky=tk.W, columnspan=1)

rad3 = tk.Radiobutton(win, text="Gray", variable=radVar, value=3, command=radCall)
rad3.grid(column=1, row=1, sticky=tk.W, columnspan=1)

rad4 = tk.Radiobutton(win, text="Negative", variable=radVar, value=4, command=radCall)
rad4.grid(column=1, row=2, sticky=tk.W, columnspan=1)

"""
#=============================================================================
#CHARTS
#=============================================================================
#-------------------------------------------------------------
fig = Figure(figsize=(12, 8), facecolor='white') 
#-------------------------------------------------------------
# axis = fig.add_subplot(111)   # 1 row,  1 column, only graph 
axis = fig.add_subplot(211)     # 2 rows, 1 column, Top graph 
#-------------------------------------------------------------
xValues = [1,2,3,4] 
yValues = [5,7,6,8] 
axis.plot(xValues, yValues) 
axis.set_xlabel('Horizontal Label') 
axis.set_ylabel('Vertical Label') 
# axis.grid()                   # default line style 
axis.grid(linestyle='-')        # solid grid lines


#-------------------------------------------------------------
def _destroyWindow():    
    win.quit()    
    win.destroy() 
#-------------------------------------------------------------
#root = tk.Tk() 
win.withdraw() 
win.protocol('WM_DELETE_WINDOW', _destroyWindow) 
#-------------------------------------------------------------
canvas = FigureCanvasTkAgg(fig, master=win) 
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1) 
#-------------------------------------------------------------
win.update() 
win.deiconify()


pyinstaller.exe --onefile --windowed --icon=app.ico --version-file=version.txt app.py

"""

# -----------------------------------------------------------------------------
# START GUI
# -----------------------------------------------------------------------------
win.mainloop()
