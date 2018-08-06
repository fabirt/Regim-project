#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Aug 06, 2018 12:40:52 PM

import tkinter as tk
import classes.Methods as met

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from classes import regim_test_1_support

# -----------------------------------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------------------------------


def vp_start_gui():

    global val, w, root
    root = Tk()
    top = REGIM(root)
    regim_test_1_support.init(root, top)
    root.mainloop()


w = None


def create_REGIM(root, *args, **kwargs):

    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = REGIM(w)
    regim_test_1_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_REGIM():
    global w
    w.destroy()
    w = None

def exit_btn():
    global root
    root.quit()
    root.destroy()
    exit()

class REGIM:
    def __init__(self, top=None):
        from PIL import ImageTk, Image
        global iminput_path, imref_path, icon_path
        icon_path = met.resource_path('icono.ico')
        imref_path = met.resource_path('000012.jpg')
        iminput_path = met.resource_path('000013.jpg')

        def do_match():
            global imref_path, iminput_path

            images_matched = met.match(imref_path, iminput_path)

            Image_matched = Image.fromarray(images_matched)
            Image_matched.thumbnail((400, 400), Image.ANTIALIAS)
            Image_matched = ImageTk.PhotoImage(Image_matched)

            self.label_reg.configure(image=Image_matched)
            self.label_reg.image = Image_matched

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        size = 200, 200
        im_reference = Image.open(imref_path)
        im_reference.thumbnail(size, Image.ANTIALIAS)
        im_reference = ImageTk.PhotoImage(im_reference)

        im_input = Image.open(iminput_path)
        im_input.thumbnail(size, Image.ANTIALIAS)
        im_input = ImageTk.PhotoImage(im_input)

        top.geometry("800x550+297+107")
        top.title("REGIM")
        top.iconbitmap(icon_path)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # Creating menu bar
        self.menuBar = Menu(top)
        top.configure(menu=self.menuBar)
        # Create menu and add menu items
        file_menu = Menu(self.menuBar, tearoff=0)
        file_menu.add_command(label="Load", command="")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=exit_btn)
        self.menuBar.add_cascade(label="File", menu=file_menu)
        # Add another menu
        help_menu = Menu(self.menuBar, tearoff=0)
        help_menu.add_command(label="About")
        self.menuBar.add_cascade(label="Help", menu=help_menu)

        self.menuFrame = LabelFrame(top)
        self.menuFrame.place(relx=0.0, rely=0.0, relheight=1.01, relwidth=0.19)
        self.menuFrame.configure(relief=GROOVE)
        self.menuFrame.configure(foreground="black")
        self.menuFrame.configure(background="#ffffff")
        self.menuFrame.configure(highlightbackground="#d9d9d9")
        self.menuFrame.configure(highlightcolor="black")
        self.menuFrame.configure(width=150)

        self.match_btn = Button(self.menuFrame, height=24, width=107, compound=tk.CENTER)
        self.match_btn.place(relx=0.1, rely=0.42, height=240, width=107, y=-12, h=23)
        self.match_btn.configure(activebackground="#d9d9d9")
        self.match_btn.configure(activeforeground="#ffffff")
        self.match_btn.configure(background="#ff6464")
        self.match_btn.configure(borderwidth="1")
        self.match_btn.configure(cursor="hand2")
        self.match_btn.configure(disabledforeground="#a3a3a3")
        self.match_btn.configure(font=font9)
        self.match_btn.configure(foreground="#ffffff")
        self.match_btn.configure(highlightbackground="#d9d9d9")
        self.match_btn.configure(highlightcolor="black")
        self.match_btn.configure(pady="0")
        self.match_btn.configure(text='Match features')

        self.Label1 = Label(self.menuFrame)
        self.Label1.place(relx=0.13, rely=0.09, height=21, width=104, y=-12, h=23)

        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='MAX_FEATURES')

        self.et_max = Entry(self.menuFrame)
        self.et_max.place(relx=0.2, rely=0.15,height=20, relwidth=0.53)
        self.et_max.configure(background="#e5e5e5")
        self.et_max.configure(disabledforeground="#a3a3a3")
        self.et_max.configure(font="TkFixedFont")
        self.et_max.configure(foreground="#000000")
        self.et_max.configure(highlightbackground="#d9d9d9")
        self.et_max.configure(highlightcolor="black")
        self.et_max.configure(insertbackground="black")
        self.et_max.configure(selectbackground="#c4c4c4")
        self.et_max.configure(selectforeground="black")

        self.Label1_1 = Label(self.menuFrame)
        self.Label1_1.place(relx=0.07, rely=0.24, height=21, width=124, y=-12, h=23)
        self.Label1_1.configure(activebackground="#ffffff")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#ffffff")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text="MATCH_PERCENT")

        self.et_percent = Entry(self.menuFrame)
        self.et_percent.place(relx=0.2, rely=0.31,height=20, relwidth=0.53)
        self.et_percent.configure(background="#e5e5e5")
        self.et_percent.configure(disabledforeground="#a3a3a3")
        self.et_percent.configure(font="TkFixedFont")
        self.et_percent.configure(foreground="#000000")
        self.et_percent.configure(highlightbackground="#d9d9d9")
        self.et_percent.configure(highlightcolor="black")
        self.et_percent.configure(insertbackground="black")
        self.et_percent.configure(selectbackground="#c4c4c4")
        self.et_percent.configure(selectforeground="black")

        self.processframe = LabelFrame(top)
        self.processframe.place(relx=0.18, rely=0.0, relheight=1.01, relwidth=0.83)
        self.processframe.configure(relief=GROOVE)
        self.processframe.configure(foreground="black")
        self.processframe.configure(background="#ffadad")
        self.processframe.configure(highlightbackground="#d9d9d9")
        self.processframe.configure(highlightcolor="black")
        self.processframe.configure(width=660)

        self.label_in = Label(self.processframe)
        self.label_in.place(relx=0.12, rely=0.07, height=200, width=200, y=-12, h=200)
        self.label_in.configure(activebackground="#f9f9f9")
        self.label_in.configure(activeforeground="black")
        self.label_in.configure(background="#ffffff")
        self.label_in.configure(disabledforeground="#a3a3a3")
        self.label_in.configure(foreground="#000000")
        self.label_in.configure(highlightbackground="#d9d9d9")
        self.label_in.configure(highlightcolor="black")
        self.label_in.configure(image=im_input)
        self.label_in.image = im_input

        self.label_ref = Label(self.processframe)
        self.label_ref.place(relx=0.58, rely=0.07, height=200, width=200, y=-12, h=200)
        self.label_ref.configure(activebackground="#f9f9f9")
        self.label_ref.configure(activeforeground="black")
        self.label_ref.configure(background="#ffffff")
        self.label_ref.configure(disabledforeground="#a3a3a3")
        self.label_ref.configure(foreground="#000000")
        self.label_ref.configure(highlightbackground="#d9d9d9")
        self.label_ref.configure(highlightcolor="black")
        self.label_ref.configure(image=im_reference)
        self.label_ref.image = im_reference

        self.label_reg = Label(self.processframe)
        self.label_reg.place(relx=0.11, rely=0.55, height=200, width=507, y=-12, h=200)
        self.label_reg.configure(activebackground="#f9f9f9")
        self.label_reg.configure(activeforeground="black")
        self.label_reg.configure(background="#ffffff")
        self.label_reg.configure(disabledforeground="#a3a3a3")
        self.label_reg.configure(foreground="#000000")
        self.label_reg.configure(highlightbackground="#d9d9d9")
        self.label_reg.configure(highlightcolor="black")

        self.match_btn.configure(command=do_match)


if __name__ == '__main__':
    vp_start_gui()
