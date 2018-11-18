#! /usr/bin/env python
#  -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
import os
import src.Tools as Tools
import src.RegistrationMethods as Reg
import src.ZoomAdvanced as Zoom
import src.Visualizer as DVisual
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import messagebox
import time
import random
import webbrowser

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


# -----------------------------------------------------------------------------
# INITIAL METHODS
# -----------------------------------------------------------------------------
def vp_start_gui():
    """Starting point when module is the main routine."""
    global root
    root = Tk()
    Regim(root)
    root.mainloop()


def create_regim(this_root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    w = Toplevel(this_root)
    top = Regim(w)
    return w, top


def destroy_regim(w):
    w.destroy()


def exit_btn():
    """Close program"""
    root.quit()
    root.destroy()
    exit()


# -----------------------------------------------------------------------------
# GLOBAL VARIABLES
# -----------------------------------------------------------------------------
"""When building .exe file, execute in the command line $path/to/project/ pyinstaller.exe specs.spec"""
"""For distribution set dist = True"""
dist = False
if dist is True:
    folder = '.'
else:
    folder = 'assets'

MY_ICON = '{0}/icon.ico'.format(folder)
MY_SEE_BTN_PATH = '{0}/see_btn.png'.format(folder)
MY_SAVE_BTN_PATH = '{0}/save_btn.png'.format(folder)
MY_DELETE_BTN_PATH = '{0}/delete_btn.png'.format(folder)
MY_EMPTY_IMAGE_PATH = '{0}/empty.jpg'.format(folder)
MY_PNG_DEST_1 = 'input_1.png'
MY_PNG_DEST_2 = 'input_2.png'
MY_OUT_DEST = 'output.png'
MY_IMREF_PATH = ''
MY_IMINPUT_PATH = ''
BASIC_COLOR = '#2857a9'

IN_SIZE = 200, 200
OUT_SIZE = 400, 400

# -----------------------------------------------------------------------------
# MAIN CLASS
# -----------------------------------------------------------------------------


class Regim:

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
                top is the toplevel containing window."""

        # Loading required assets and paths. Initializing variables
        self.icon_path = Tools.resource_path(MY_ICON)
        self.see_btn_path = Tools.resource_path(MY_SEE_BTN_PATH)
        self.save_btn_path = Tools.resource_path(MY_SAVE_BTN_PATH)
        self.delete_btn_path = Tools.resource_path(MY_DELETE_BTN_PATH)
        self.empty_image_path = Tools.resource_path(MY_EMPTY_IMAGE_PATH)
        self.png_dest_1 = MY_PNG_DEST_1
        self.png_dest_2 = MY_PNG_DEST_2
        self.im_fixed_path = None
        self.im_moving_path = None
        self.png_fixed_img = None
        self.png_moving_img = None
        self.output_image = None
        self.fixed_object = None
        self.moving_object = None
        self.reg_object = None
        self.bw_object = None
        self.bw_image = None
        self.radio_var = IntVar()
        self.png_path_list = [self.png_dest_1, self.png_dest_2, MY_OUT_DEST, MY_OUT_DEST]

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family Verdana -size 9 -weight normal -slant roman" \
                 " -underline 0 -overstrike 0"
        font11 = "-family Verdana -size 11 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font13 = "-family Verdana -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        # Creating all the GUI
        top.geometry("1200x650+127+8")
        top.title("Regim")
        top.iconbitmap(self.icon_path)
        top.resizable(False, False)
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#ffffff")
        top.configure(highlightcolor="black")

        # Menu bar configuration
        self.menubar = Menu(top, font="TkMenuFont")
        top.configure(menu=self.menubar)

        self.file = Menu(top, tearoff=0)
        self.menubar.add_cascade(
            menu=self.file,
            font="TkMenuFont",
            label="File"
        )
        self.file.add_command(
            font="TkMenuFont",
            label="Exit",
            command=exit_btn
        )

        self.help = Menu(top, tearoff=0)

        self.menubar.add_cascade(
            menu=self.help,
            font="TkMenuFont",
            foreground="#000000",
            label="Help"
        )
        self.help.add_command(
            font="TkMenuFont",
            foreground="#000000",
            label="About",
            command=self.open_browser
        )

        # Frames configuration
        self.frame_side = Frame(top)
        self.frame_side.place(relx=-0.02, rely=-0.02, relheight=1.01, relwidth=0.16)
        self.frame_side.configure(relief=SUNKEN)
        self.frame_side.configure(borderwidth="1")
        self.frame_side.configure(relief=SUNKEN)
        self.frame_side.configure(background="#202020")  # color #383838
        self.frame_side.configure(highlightbackground="#ffffff")
        self.frame_side.configure(highlightcolor="black")
        self.frame_side.configure(width=215)

        # Registration button
        self.reg_button = Button(self.frame_side)
        self.reg_button.place(relx=0.16, rely=0.87, height=34, width=150)
        self.reg_button.configure(activebackground="#0f306a")
        self.reg_button.configure(activeforeground="white")
        self.reg_button.configure(activeforeground="#ffffff")
        self.reg_button.configure(background=BASIC_COLOR)
        self.reg_button.configure(borderwidth="0")
        self.reg_button.configure(disabledforeground="#a3a3a3")
        self.reg_button.configure(font=font13)
        self.reg_button.configure(foreground="#ffffff")
        self.reg_button.configure(highlightbackground="#d9d9d9")
        self.reg_button.configure(highlightcolor="black")
        self.reg_button.configure(overrelief="sunken")
        self.reg_button.configure(pady="0")
        self.reg_button.configure(relief=FLAT)
        self.reg_button.configure(text='Registration')
        self.reg_button.configure(cursor="hand2")
        self.reg_button.configure(command=self.do_registration)

        # Side menu
        self.label_side = LabelFrame(self.frame_side)
        self.label_side.place(relx=0.16, rely=0.085, relheight=0.755, relwidth=0.8)
        self.label_side.configure(borderwidth="1")
        self.label_side.configure(foreground="black")
        self.label_side.configure(relief=FLAT)
        self.label_side.configure(background="#393939")  # color #585858
        self.label_side.configure(width=150)

        # Frame inputs and output
        self.frame_process = Frame(top)
        self.frame_process.place(relx=0.137, rely=0.02, relheight=1.02, relwidth=0.883)
        self.frame_process.configure(borderwidth="1")
        self.frame_process.configure(background="#5d5f60")
        self.frame_process.configure(highlightbackground="#000000")
        self.frame_process.configure(highlightcolor="#ffffff")
        self.frame_process.configure(width=805)

        # Frame DICOM info 1
        self.frame_dicom_info_1 = Frame(self.frame_process)
        self.frame_dicom_info_1.place(relx=0.28, rely=0.08, height=200, width=140)
        self.frame_dicom_info_1.configure(borderwidth="0")
        self.frame_dicom_info_1.configure(background="#ccc")
        self.frame_dicom_info_1.configure(highlightbackground="#000000")
        self.frame_dicom_info_1.configure(highlightcolor="#ffffff")

        # Frame DICOM info 2
        self.frame_dicom_info_2 = Frame(self.frame_process)
        self.frame_dicom_info_2.place(relx=0.28, rely=0.51, height=200, width=140)
        self.frame_dicom_info_2.configure(borderwidth="0")
        self.frame_dicom_info_2.configure(background="#ccc")
        self.frame_dicom_info_2.configure(highlightbackground="#000000")
        self.frame_dicom_info_2.configure(highlightcolor="#ffffff")

        # Frame Outputs
        self.frame_outputs = Frame(self.frame_process)
        self.frame_outputs.place(relx=0.47, rely=0, relheight=1.02)
        self.frame_outputs.configure(borderwidth="0")
        self.frame_outputs.configure(background="#444749")
        self.frame_outputs.configure(highlightbackground="#000000")
        self.frame_outputs.configure(highlightcolor="#ffffff")
        self.frame_outputs.configure(width=564)

        # Registered image frame
        self.frame_registered = Frame(self.frame_outputs)
        self.frame_registered.place(relx=0.11, rely=0.08, height=202, width=202)
        self.frame_registered.configure(borderwidth="0")
        self.frame_registered.configure(background="#ccc")
        self.frame_registered.configure(highlightbackground="#000000")
        self.frame_registered.configure(highlightcolor="#ffffff")

        # Registered B&W image frame
        self.frame_bw = Frame(self.frame_outputs)
        self.frame_bw.place(relx=0.11, rely=0.498, height=202, width=202)
        self.frame_bw.configure(borderwidth="0")
        self.frame_bw.configure(background="#ccc")
        self.frame_bw.configure(highlightbackground="#000000")
        self.frame_bw.configure(highlightcolor="#ffffff")

        # Data frame
        self.frame_data = Frame(self.frame_outputs)
        self.frame_data.place(relx=0.59, rely=0.08, height=202, width=122)
        self.frame_data.configure(borderwidth="0")
        self.frame_data.configure(background="#ccc")
        self.frame_data.configure(highlightbackground="#000000")
        self.frame_data.configure(highlightcolor="#ffffff")

        # Right frame
        self.frame_right = Frame(self.frame_process)
        self.frame_right.place(relx=0.946, rely=0, relheight=1.02)
        self.frame_right.configure(borderwidth="0")
        self.frame_right.configure(background="#1d1f21")
        self.frame_right.configure(highlightbackground="#000000")
        self.frame_right.configure(highlightcolor="#ffffff")
        self.frame_right.configure(width=40)

        # Frame slider 1
        self.frame_slider_1 = Frame(self.frame_process)
        self.frame_slider_1.place(relx=0.05, rely=0.41, height=17, width=200)
        self.frame_slider_1.configure(borderwidth="0")
        self.frame_slider_1.configure(background="#000")
        self.frame_slider_1.configure(highlightbackground="#000000")
        self.frame_slider_1.configure(highlightcolor="#ffffff")

        # Brightness slider 1
        self.scale_br_fixed = Scale(self.frame_slider_1, from_=0, to=4, orient=HORIZONTAL, resolution=0.2)
        self.scale_br_fixed.place(relx=0.0, rely=-1.2, width=200)
        self.scale_br_fixed.configure(background="#393939")
        self.scale_br_fixed.configure(activebackground="#202020")
        self.scale_br_fixed.configure(borderwidth="0")
        self.scale_br_fixed.configure(command=lambda _: self.enhance_image(self.fixed_object,
                                                                                    self.png_fixed_img,
                                                                                    self.scale_br_fixed,
                                                                                    None))
        self.scale_br_fixed.set(1)

        # Frame slider 2
        self.frame_slider_2 = Frame(self.frame_process)
        self.frame_slider_2.place(relx=0.05, rely=0.84, height=17, width=200)
        self.frame_slider_2.configure(borderwidth="0")
        self.frame_slider_2.configure(background="#000")
        self.frame_slider_2.configure(highlightbackground="#000000")
        self.frame_slider_2.configure(highlightcolor="#ffffff")

        # Brightness slider 2
        self.scale_br_moving = Scale(self.frame_slider_2, from_=0, to=4, orient=HORIZONTAL, resolution=0.2)
        self.scale_br_moving.place(relx=0.0, rely=-1.2, width=200)
        self.scale_br_moving.configure(background="#393939")
        self.scale_br_moving.configure(activebackground="#202020")
        self.scale_br_moving.configure(borderwidth="0")
        self.scale_br_moving.configure(command=lambda _: self.enhance_image(self.moving_object,
                                                                                    self.png_moving_img,
                                                                                    self.scale_br_moving,
                                                                                    None))
        self.scale_br_moving.set(1)

        # Frame slider 3
        self.frame_slider_3 = Frame(self.frame_outputs)
        self.frame_slider_3.place(relx=0.11, rely=0.826, height=17, width=200)
        self.frame_slider_3.configure(borderwidth="0")
        self.frame_slider_3.configure(background="#000")
        self.frame_slider_3.configure(highlightbackground="#000000")
        self.frame_slider_3.configure(highlightcolor="#ffffff")

        # Brightness slider 3
        self.scale_br_bw = Scale(self.frame_slider_3, from_=0, to=4, orient=HORIZONTAL, resolution=0.2)
        self.scale_br_bw.place(relx=0.0, rely=-1.2, width=200)
        self.scale_br_bw.configure(background="#393939")
        self.scale_br_bw.configure(activebackground="#202020")
        self.scale_br_bw.configure(borderwidth="0")
        self.scale_br_bw.configure(command=lambda _: self.enhance_image(self.bw_object,
                                                                                    self.bw_image,
                                                                                    self.scale_br_bw,
                                                                                    None))
        self.scale_br_bw.set(1)

        # Frame slider 4
        self.frame_slider_4 = Frame(self.frame_outputs)
        self.frame_slider_4.place(relx=0.11, rely=0.405, height=17, width=200)
        self.frame_slider_4.configure(borderwidth="0")
        self.frame_slider_4.configure(background="#000")
        self.frame_slider_4.configure(highlightbackground="#000000")
        self.frame_slider_4.configure(highlightcolor="#ffffff")

        # Brightness slider 4
        self.scale_br_registered = Scale(self.frame_slider_4, from_=0, to=4, orient=HORIZONTAL, resolution=0.2)
        self.scale_br_registered.place(relx=0.0, rely=-1.2, width=200)
        self.scale_br_registered.configure(background="#393939")
        self.scale_br_registered.configure(activebackground="#202020")
        self.scale_br_registered.configure(borderwidth="0")
        self.scale_br_registered.configure(command=lambda _: self.enhance_image(self.reg_object,
                                                                                    self.output_image,
                                                                                    self.scale_br_registered,
                                                                                None))
        self.scale_br_registered.set(1)

        # Frame fixed image
        self.frame_fixed = Frame(self.frame_process)
        self.frame_fixed.place(relx=0.05, rely=0.08, height=200, width=200)
        self.frame_fixed.configure(borderwidth="1")
        self.frame_fixed.configure(background=BASIC_COLOR)  # color #383838
        self.frame_fixed.configure(cursor="fleur")

        # Frame moving image
        self.frame_moving = Frame(self.frame_process)
        self.frame_moving.place(relx=0.05, rely=0.51, height=200, width=200)
        self.frame_moving.configure(borderwidth="1")
        self.frame_moving.configure(background=BASIC_COLOR)  # color #383838
        self.frame_moving.configure(cursor="fleur")

        # Frame inner bw image
        self.frame_bw_editable = Frame(self.frame_bw)
        self.frame_bw_editable.place(relx=0.003, rely=0.003, height=200, width=200)
        self.frame_bw_editable.configure(borderwidth="0")
        self.frame_bw_editable.configure(background="#444749")  # color #383838
        self.frame_bw_editable.configure(cursor="fleur")

        # Frame inner registered image
        self.frame_registered_editable = Frame(self.frame_registered)
        self.frame_registered_editable.place(relx=0.003, rely=0.003, height=200, width=200)
        self.frame_registered_editable.configure(borderwidth="0")
        self.frame_registered_editable.configure(background="#444749")  # color #383838
        self.frame_registered_editable.configure(cursor="fleur")

        # Data label
        self.label_data = Label(self.frame_data)
        self.label_data.place(relx=0.005, rely=0.003, height=30, width=120)
        self.label_data.configure(background="#444749")
        self.label_data.configure(cursor="")
        self.label_data.configure(font=font9)
        self.label_data.configure(foreground="#ccc")
        self.label_data.configure(text='Data')

        # Info label
        self.label_info = Label(self.frame_data)
        self.label_info.place(relx=0.005, rely=0.155, height=170, width=120)
        self.label_info.configure(background="#444749")
        self.label_info.configure(cursor="")
        self.label_info.configure(font=font9)
        self.label_info.configure(foreground="#ccc")
        self.label_info.configure(wraplength=100)

        # Title DICOM info 1
        self.label_title_1 = Label(self.frame_dicom_info_1)
        self.label_title_1.place(relx=0.005, rely=0.003, height=30, width=138)
        self.label_title_1.configure(background="#5d5f60")
        self.label_title_1.configure(cursor="")
        self.label_title_1.configure(font=font9)
        self.label_title_1.configure(foreground="#ccc")
        self.label_title_1.configure(text='DICOM info')

        # Label DICOM data 1
        self.label_dicom_data_1 = Label(self.frame_dicom_info_1)
        self.label_dicom_data_1.place(relx=0.005, rely=0.145, height=170, width=138)
        self.label_dicom_data_1.configure(background="#5d5f60")
        self.label_dicom_data_1.configure(cursor="")
        self.label_dicom_data_1.configure(font=font9)
        self.label_dicom_data_1.configure(foreground="#ccc")
        self.label_dicom_data_1.configure(text='')
        self.label_dicom_data_1.configure(wraplength=120)

        # Title DICOM info 2
        self.label_title_2 = Label(self.frame_dicom_info_2)
        self.label_title_2.place(relx=0.005, rely=0.003, height=30, width=138)
        self.label_title_2.configure(background="#5d5f60")
        self.label_title_2.configure(cursor="")
        self.label_title_2.configure(font=font9)
        self.label_title_2.configure(foreground="#ccc")
        self.label_title_2.configure(text='DICOM info')

        # Label DICOM data 2
        self.label_dicom_data_2 = Label(self.frame_dicom_info_2)
        self.label_dicom_data_2.place(relx=0.005, rely=0.145, height=170, width=138)
        self.label_dicom_data_2.configure(background="#5d5f60")
        self.label_dicom_data_2.configure(cursor="")
        self.label_dicom_data_2.configure(font=font9)
        self.label_dicom_data_2.configure(foreground="#ccc")
        self.label_dicom_data_2.configure(text='')
        self.label_dicom_data_2.configure(wraplength=120)

        # Frame foot
        self.frame_foot = Frame(top)
        self.frame_foot.place(relx=-0.01, rely=0.94, relheight=0.07, relwidth=1.02)
        self.frame_foot.configure(relief=SUNKEN)
        self.frame_foot.configure(borderwidth="1")
        self.frame_foot.configure(relief=SUNKEN)
        self.frame_foot.configure(background="#202020")  # color #383838
        self.frame_foot.configure(highlightbackground="#d9d9d9")
        self.frame_foot.configure(highlightcolor="#ffffff")
        self.frame_foot.configure(width=995)

        # Top frame
        self.frame_top = Frame(top)
        self.frame_top.place(relx=-0.01, rely=-0.1, relheight=0.14, relwidth=1.03)
        self.frame_top.configure(relief=RIDGE)
        self.frame_top.configure(borderwidth="1")
        self.frame_top.configure(relief=RIDGE)
        self.frame_top.configure(background="#202020")
        self.frame_top.configure(highlightbackground="#d9d9d9")
        self.frame_top.configure(highlightcolor="#ffffff")
        self.frame_top.configure(width=1005)

        # SEE button
        self.see_button = Button(self.frame_right)
        self.see_button.place(relx=0.05, rely=0.05, height=30, width=30)
        self.see_button.configure(activebackground="#1d1f21")
        self.see_button.configure(background="#d9d9d9")
        self.see_button.configure(borderwidth="0")
        self.see_button.configure(cursor="hand2")
        self._see_img = PhotoImage(file=self.see_btn_path)
        self.see_button.configure(image=self._see_img)
        self.see_button.configure(command=self.open_visualizer)

        # SAVE AS button
        self.save_button = Button(self.frame_right)
        self.save_button.place(relx=0.05, rely=0.73, height=30, width=30)
        self.save_button.configure(activebackground="#fff")
        self.save_button.configure(background="#d9d9d9")
        self.save_button.configure(borderwidth="0")
        self.save_button.configure(cursor="hand2")
        self._save_img = PhotoImage(file=self.save_btn_path)
        self.save_button.configure(image=self._save_img)
        self.save_button.configure(command=self.save_file)

        # DELETE button
        self.delete_button = Button(self.frame_right)
        self.delete_button.place(relx=0.05, rely=0.82, height=30, width=30)
        self.delete_button.configure(activebackground="#fff")
        self.delete_button.configure(background="#d9d9d9")
        self.delete_button.configure(borderwidth="0")
        self.delete_button.configure(cursor="hand2")
        self._del_img = PhotoImage(file=self.delete_btn_path)
        self.delete_button.configure(image=self._del_img)
        self.delete_button.configure(command=self.delete_files)

        # Left menu labels
        self.select_input_label = Label(self.label_side)
        self.select_input_label.place(relx=0, rely=0, height=30, width=150)
        self.select_input_label.configure(background=BASIC_COLOR)
        self.select_input_label.configure(foreground="#fff")
        self.select_input_label.configure(font=font11)
        self.select_input_label.configure(text="Select inputs")
        # Select fixed image button
        self.select_fixed_btn = Button(self.label_side)
        self.select_fixed_btn.place(relx=0, rely=0.08, height=26, width=150)
        self.select_fixed_btn.configure(background="#393939")
        self.select_fixed_btn.configure(activebackground="#474747")
        self.select_fixed_btn.configure(activeforeground="#cccccc")
        self.select_fixed_btn.configure(foreground="#ccc")
        self.select_fixed_btn.configure(font=font11)
        self.select_fixed_btn.configure(text="Fixed image")
        self.select_fixed_btn.configure(borderwidth="0")
        self.select_fixed_btn.configure(cursor="hand2")
        self.select_fixed_btn.configure(command=self.add_fixed_image)
        # Select moving image button
        self.select_moving_btn = Button(self.label_side)
        self.select_moving_btn.place(relx=0, rely=0.15, height=26, width=150)
        self.select_moving_btn.configure(background="#393939")
        self.select_moving_btn.configure(activebackground="#474747")
        self.select_moving_btn.configure(activeforeground="#cccccc")
        self.select_moving_btn.configure(foreground="#ccc")
        self.select_moving_btn.configure(font=font11)
        self.select_moving_btn.configure(text="Moving image")
        self.select_moving_btn.configure(borderwidth="0")
        self.select_moving_btn.configure(cursor="hand2")
        self.select_moving_btn.configure(command=self.add_moving_image)
        # Left method label
        self.select_method_label = Label(self.label_side)
        self.select_method_label.place(relx=0, rely=0.23, height=30, width=150)
        self.select_method_label.configure(background=BASIC_COLOR)
        self.select_method_label.configure(foreground="#fff")
        self.select_method_label.configure(font=font11)
        self.select_method_label.configure(text="Regim methods")
        # Select displacement method button
        self.select_disp_btn = Radiobutton(self.label_side, variable=self.radio_var, value=1)
        self.select_disp_btn.place(relx=0, rely=0.294, height=38, width=150)
        self.select_disp_btn.configure(selectcolor='#515151', indicatoron=False)
        self.select_disp_btn.configure(background="#393939")
        self.select_disp_btn.configure(foreground="#ccc")
        self.select_disp_btn.configure(activebackground="#474747")
        self.select_disp_btn.configure(activeforeground="#ccc")
        self.select_disp_btn.configure(font=font11)
        self.select_disp_btn.configure(text="Displacement")
        self.select_disp_btn.configure(borderwidth="0")
        self.select_disp_btn.configure(cursor="hand2")
        self.select_disp_btn.select()
        # Select restrictive method button
        self.select_restrc_btn = Radiobutton(self.label_side, variable=self.radio_var, value=2)
        self.select_restrc_btn.place(relx=0, rely=0.37, height=38, width=150)
        self.select_restrc_btn.configure(selectcolor='#515151', indicatoron=False)
        self.select_restrc_btn.configure(background="#393939")
        self.select_restrc_btn.configure(foreground="#ccc")
        self.select_restrc_btn.configure(activebackground="#474747")
        self.select_restrc_btn.configure(activeforeground="#ccc")
        self.select_restrc_btn.configure(font=font11)
        self.select_restrc_btn.configure(text="Restrictive")
        self.select_restrc_btn.configure(borderwidth="0")
        self.select_restrc_btn.configure(cursor="hand2")
        # Left parameters label
        self.select_parameters_label = Label(self.label_side)
        self.select_parameters_label.place(relx=0, rely=0.45, height=30, width=150)
        self.select_parameters_label.configure(background=BASIC_COLOR)
        self.select_parameters_label.configure(foreground="#fff")
        self.select_parameters_label.configure(font=font11)
        self.select_parameters_label.configure(text="Parameters")
        # Iterations label
        self.iterations_input = Label(self.label_side)
        self.iterations_input.place(relx=0, rely=0.53, height=26, width=150)
        self.iterations_input.configure(background="#393939")
        self.iterations_input.configure(foreground="#ccc")
        self.iterations_input.configure(activebackground="#474747")
        self.iterations_input.configure(activeforeground="#cccccc")
        self.iterations_input.configure(font=font11)
        self.iterations_input.configure(text="Iterations")
        self.iterations_input.configure(borderwidth="0")
        # Max iterations entry
        self.iterations_entry = Entry(self.label_side)
        self.iterations_entry.place(relx=0.28, rely=0.61, height=17, width=60)
        self.iterations_entry.configure(background="#ccc")
        self.iterations_entry.configure(disabledforeground="#a3a3a3")
        self.iterations_entry.configure(foreground="#000")
        self.iterations_entry.configure(font=font11)
        self.iterations_entry.configure(borderwidth="0")
        self.iterations_entry.insert(0, "100")

        # Progress bar
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", troughcolor='#202020', background=BASIC_COLOR)
        self.progress_bar = ttk.Progressbar(self.frame_foot,
                                            style="red.Horizontal.TProgressbar",
                                            orient='horizontal',
                                            mode='determinate')
        self.progress_bar.place(relx=0, rely=0, height=40, width=1215)
        self.mask = Label(self.frame_foot)
        self.mask.place(relx=0, rely=0, height=31, width=1215)
        self.mask.configure(background='#202020')

        # Success bar
        ss = ttk.Style()
        ss.theme_use('clam')
        ss.configure("blue.Horizontal.TProgressbar", troughcolor='#202020', background=BASIC_COLOR)
        self.success_bar = ttk.Progressbar(self.frame_data,
                                            style="blue.Horizontal.TProgressbar",
                                            orient='horizontal',
                                            mode='determinate')
        self.success_bar.place(relx=0.1, rely=0.8, height=20, width=100)

    # -----------------------------------------------------------------------------
    # EVENTS
    # -----------------------------------------------------------------------------

    def add_fixed_image(self):
        """Open an image file and show it in the GUI"""
        from PIL import Image
        self.png_dest_1 = MY_PNG_DEST_1
        # Searching file
        try:
            self.im_fixed_path = askopenfilename(
                        initialdir=".",
                        filetypes=(
                            ("Dicom (*.DCM)", "*.dcm"),
                            ("JPEG (*.JPG)", "*.jpg*"),
                            ("PNG (*.PNG)", "*.png*")
                        ),
                        title="Choose image 1."
                       )
            # Converting .dcm file to .png for manipulation
            if self.im_fixed_path[-3:] == 'dcm':
                convert = Tools.Convert()
                convert.dicom_to_png(self.im_fixed_path, self.png_dest_1)
                dicom_info = convert.dicom_file_info
                self.label_dicom_data_1.configure(text=dicom_info)
                self.png_path_list[0] = self.png_dest_1
            else:
                self.png_dest_1 = self.im_fixed_path
                self.png_path_list[0] = self.im_fixed_path
                self.label_dicom_data_1.configure(text="None")

            # Resize and place it in the Frame
            self.png_fixed_img = Image.open(self.png_dest_1)
            self.png_fixed_img.thumbnail(IN_SIZE, Image.ANTIALIAS)

            self.fixed_object = Zoom.ZoomAdvanced(self.frame_fixed, self.png_fixed_img)

            self.im_fixed_path = self.png_dest_1

            self.scale_br_fixed.set(1)
        except:
            pass

    def add_moving_image(self):
        """Open an image file and show it in the GUI"""
        from PIL import Image
        self.png_dest_2 = MY_PNG_DEST_2
        try:
            # Searching file
            self.im_moving_path = askopenfilename(
                            initialdir=".",
                            filetypes=(
                                ("Dicom (*.DCM)", "*.dcm"),
                                ("JPEG (*.JPG)", "*.jpg*"),
                                ("PNG (*.PNG)", "*.png*")
                            ),
                            title="Choose image 2."
                            )
            # Converting .dcm file to .png for manipulation
            if self.im_moving_path[-3:] == 'dcm':
                convert = Tools.Convert()
                convert.dicom_to_png(self.im_moving_path, self.png_dest_2)
                dicom_info = convert.dicom_file_info
                self.label_dicom_data_2.configure(text=dicom_info)
                self.png_path_list[1] = self.png_dest_2
            else:
                self.png_dest_2 = self.im_moving_path
                self.png_path_list[1] = self.im_moving_path
                self.label_dicom_data_2.configure(text="None")

            # resize and place it in the Frame
            self.png_moving_img = Image.open(self.png_dest_2)
            self.png_moving_img.thumbnail(IN_SIZE, Image.ANTIALIAS)

            self.moving_object = Zoom.ZoomAdvanced(self.frame_moving, self.png_moving_img)

            self.im_moving_path = self.png_dest_2

            self.scale_br_moving.set(1)

        except:
            pass

    def do_registration(self):
        """Do the registration for the fixed and moving image"""
        from PIL import Image
        try:
            method = self.radio_var.get()
            max_iterations = int(self.iterations_entry.get())
            if max_iterations <= 0:
                int("abc")
            elif self.fixed_object is None or self.moving_object is None:
                messagebox.showinfo("Warning!", "Empty inputs")
                return

            self.success_bar['maximum'] = 100
            self.progress_bar['maximum'] = 100
            self.run_progress_bar(1, random.randint(30, 60))

            my_imreg = Reg.Imreg(self.png_dest_1, self.png_dest_2)

            if method == 1:
                registered_image, reg_nda = my_imreg.image_registration_method_displacement(max_iterations)
            else:
                registered_image, reg_nda = my_imreg.image_registration_method_restrictive(max_iterations)

            self.output_image = registered_image
            self.output_image.save(MY_OUT_DEST)

            self.progress_bar['value'] = random.randint(70, 90)
            self.progress_bar.update()
            time.sleep(0.1)

            self.output_image.thumbnail(IN_SIZE, Image.ANTIALIAS)

            copy = registered_image
            self.bw_image = copy.convert("L")

            self.progress_bar['value'] = 100
            self.progress_bar.update()
            time.sleep(0.2)

            self.bw_object = Zoom.ZoomAdvanced(self.frame_bw_editable, self.bw_image)
            self.reg_object = Zoom.ZoomAdvanced(self.frame_registered_editable, self.output_image)

            metric = my_imreg.info_data.split(" Metric value:" + "\n")[1]
            percentage = (float(metric)*100) / -1.8
            if percentage >= 100:
                percentage = 100
                data_string = my_imreg.info_data + "\n\n(" + str(percentage)[0:3] + "%)"
            else:
                data_string = my_imreg.info_data + "\n\n(" + str(percentage)[0:2] + "%)"

            self.label_info.configure(text=data_string)

            self.success_bar['value'] = (float(metric)*100) / -1.5
            self.success_bar.update()

            self.scale_br_bw.set(1)
            self.scale_br_registered.set(1)

            self.progress_bar['value'] = 0

        except ValueError:
            title = "Value Error"
            message = "Max iterations must be a positive integer!"
            messagebox.showerror(title, message)

    def run_progress_bar(self, start, stop):
        """Run the progress bar"""
        for i in range(start, stop):
            time.sleep(0.015)
            self.progress_bar['value'] = i
            self.progress_bar.update()

    def save_file(self):
        file_types = [("PNG (*.PNG)", "*.png*")]
        # define options for saving
        options = {
            'defaultextension': ".png",
            'filetypes': file_types,
            'initialfile': "OutputImage",
            'title': "Save output image"
        }
        if self.bw_object is not None:
            """Save registered image"""
            f = asksaveasfile(mode='w', **options)
            if f is None:  # asksaveasfile return 'None' if dialog closed with "cancel".
                return
            saving_path = f.name
            self.bw_image.save(saving_path)
            f.close()
        else:
            title = "Impossible action"
            message = "No output file to save"
            messagebox.showwarning(title, message)

    def delete_files(self):
        title = "Delete files"
        message = "Are you sure you want to permanently delete the assets files?"
        answer = messagebox.askquestion(title, message, icon='warning')
        if answer == "yes":
            if os.path.exists(MY_PNG_DEST_1):
                os.remove(MY_PNG_DEST_1)
                self.fixed_object = None
                self.label_dicom_data_1.configure(text="")
                for child in self.frame_fixed.winfo_children():
                    child.destroy()
            if os.path.exists(MY_PNG_DEST_2):
                os.remove(MY_PNG_DEST_2)
                self.moving_object = None
                self.label_dicom_data_2.configure(text="")
                for child in self.frame_moving.winfo_children():
                    child.destroy()
            if os.path.exists(MY_OUT_DEST):
                os.remove(MY_OUT_DEST)
                self.bw_object = None
                self.reg_object = None
                self.label_info.configure(text="")
                self.success_bar['value'] = 0
                self.success_bar.update()
                for child in self.frame_bw_editable.winfo_children():
                    child.destroy()
                for child in self.frame_registered_editable.winfo_children():
                    child.destroy()
        else:
            pass

    def open_visualizer(self):
        """Open image visualizer (DVisual)"""
        if self.reg_object is not None:
            visual = Tk()
            DVisual.DVisual(visual,
                            self.png_fixed_img,
                            self.png_moving_img,
                            self.output_image,
                            self.bw_image,
                            self.png_path_list)
            visual.mainloop()
        else:
            title = "Incomplete task"
            message = "No image files to visualize"
            messagebox.showwarning(title, message)

    @staticmethod
    def enhance_image(zoom_object, image, br_scale, sh_scale):
        """Edit image brightness, contrast and color"""
        from PIL import ImageEnhance
        if zoom_object is not None:
            brightness = br_scale.get()

            if sh_scale is not None:
                sharpness = sh_scale.get()
            else:
                sharpness = 1

            enhancer = ImageEnhance.Brightness(image)
            edited_img = enhancer.enhance(brightness)

            enhancer = ImageEnhance.Sharpness(edited_img)
            edited_img = enhancer.enhance(sharpness)

            zoom_object.set_image(edited_img)
            zoom_object.show_image()

    @staticmethod
    def open_browser():
        """Go to Regim web page"""
        url = "https://fabirt.github.io/Regim-project/Regim-Web/doc.html"
        webbrowser.open(url)


if __name__ == '__main__':
    vp_start_gui()
