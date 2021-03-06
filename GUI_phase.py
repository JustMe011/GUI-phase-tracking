#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 24, 2018 03:47:50 AM CEST  platform: Linux

import sys

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

import GUI_phase_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    GUI_phase_support.set_Tk_var()
    top = PHASE_TRACKING_GUI (root)
    GUI_phase_support.init(root, top)
    root.mainloop()

w = None
def create_PHASE_TRACKING_GUI(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    GUI_phase_support.set_Tk_var()
    top = PHASE_TRACKING_GUI (w)
    GUI_phase_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PHASE_TRACKING_GUI():
    global w
    w.destroy()
    w = None


class PHASE_TRACKING_GUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Bitstream Vera Sans} -size 12 -weight normal"  \
            " -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1351x706+-3+-8")
        top.title("PHASE TRACKING GUI")
        top.configure(highlightcolor="black")



        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.014, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(width=300)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="LOAD",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#a8a8a8")
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="CHANNELS",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#a8a8a8")
        self.TNotebook1_t2 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="CHs PSD",compound="none",underline="-1",)
        self.TNotebook1_t2.configure(background="#a8a8a8")
        self.TNotebook1_t3 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="RECOVERY",compound="none",underline="-1",)
        self.TNotebook1_t3.configure(borderwidth="2")
        self.TNotebook1_t3.configure(background="#a8a8a8")

        self.Frame2 = Frame(self.TNotebook1_t0)
        self.Frame2.place(relx=0.126, rely=0.044, relheight=0.169
                , relwidth=0.738)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(width=995)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.322, rely=0.087, height=29, width=251)
        self.Label1.configure(activebackground="#841216")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(background="#d8d582")
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(justify=RIGHT)
        self.Label1.configure(relief=SUNKEN)
        self.Label1.configure(text='''Load from file''')

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.03, rely=0.609, height=27, width=68)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Search''')
        self.Button1.bind('<Button-1>',lambda e:GUI_phase_support.Search_pressed(e))

        self.Text1 = Text(self.Frame2)
        self.Text1.place(relx=0.121, rely=0.609, relheight=0.226, relwidth=0.257)

        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=256)
        self.Text1.configure(wrap=WORD)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.402, rely=0.609, height=21, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(borderwidth="2")
        self.Label3.configure(text='''Delimiter:''')

        self.Entry1 = Entry(self.Frame2)
        self.Entry1.place(relx=0.482, rely=0.609,height=21, relwidth=0.036)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(textvariable=GUI_phase_support.cont_delim)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.905, rely=0.261, height=34, width=69)
        self.Button3.configure(activebackground="#d9d9d9")
        self._img1 = PhotoImage(file="./upload_button.png")
        self.Button3.configure(image=self._img1)
        self.Button3.configure(text='''Button''')
        self.Button3.bind('<Button-1>',lambda e:GUI_phase_support.LoadFile_pressed(e))

        self.Label8 = Label(self.Frame2)
        self.Label8.place(relx=0.543, rely=0.609, height=19, width=50)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(borderwidth="2")
        self.Label8.configure(text='''Chunck:''')

        self.Entry8 = Entry(self.Frame2)
        self.Entry8.place(relx=0.603, rely=0.609,height=21, relwidth=0.076)
        self.Entry8.configure(background="white")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(textvariable=GUI_phase_support.cont_chunck)

        self.Label11 = Label(self.Frame2)
        self.Label11.place(relx=0.915, rely=0.609, height=19, width=36)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(borderwidth="2")
        self.Label11.configure(textvariable=GUI_phase_support.upload_check)

        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.Checkbutton3.place(relx=0.754, rely=0.087, relheight=0.183
                , relwidth=0.068)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''LO mix''')
        self.Checkbutton3.configure(variable=GUI_phase_support.lo_mix)

        self.Entry12 = Entry(self.Frame2)
        self.Entry12.place(relx=0.709, rely=0.261,height=21, relwidth=0.117)
        self.Entry12.configure(background="white")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(selectbackground="#c4c4c4")
        self.Entry12.configure(textvariable=GUI_phase_support.freq_lo)

        self.Label15 = Label(self.Frame2)
        self.Label15.place(relx=0.834, rely=0.261, height=19, width=19)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(borderwidth="2")
        self.Label15.configure(text='''Hz''')

        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.Checkbutton4.place(relx=0.754, rely=0.522, relheight=0.183
                , relwidth=0.093)
        self.Checkbutton4.configure(activebackground="#d9d9d9")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''Downsamp''')
        self.Checkbutton4.configure(variable=GUI_phase_support.downsamp)

        self.Entry6 = Entry(self.Frame2)
        self.Entry6.place(relx=0.749, rely=0.739,height=21, relwidth=0.036)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(textvariable=GUI_phase_support.num_down)

        self.Label17 = Label(self.Frame2)
        self.Label17.place(relx=0.794, rely=0.696, height=19, width=32)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(text='''num''')

        self.Frame3 = Frame(self.TNotebook1_t0)
        self.Frame3.place(relx=0.126, rely=0.235, relheight=0.682
                , relwidth=0.738)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(width=995)

        self.Label2 = Label(self.Frame3)
        self.Label2.place(relx=0.322, rely=0.043, height=29, width=251)
        self.Label2.configure(activebackground="#841216")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(background="#d8d582")
        self.Label2.configure(borderwidth="2")
        self.Label2.configure(justify=RIGHT)
        self.Label2.configure(relief=SUNKEN)
        self.Label2.configure(text='''Load from simulated data''')

        self.Label4 = Label(self.Frame3)
        self.Label4.place(relx=0.02, rely=0.161, height=21, width=23)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(borderwidth="2")
        self.Label4.configure(text='''DE''')

        self.Label5 = Label(self.Frame3)
        self.Label5.place(relx=0.02, rely=0.323, height=21, width=21)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(borderwidth="2")
        self.Label5.configure(text='''TE''')

        self.Label6 = Label(self.Frame3)
        self.Label6.place(relx=0.02, rely=0.473, height=21, width=22)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(borderwidth="2")
        self.Label6.configure(text='''PH''')

        self.Entry2 = Entry(self.Frame3)
        self.Entry2.place(relx=0.07, rely=0.172,height=21, relwidth=0.201)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(textvariable=GUI_phase_support.eq_de)

        self.Entry3 = Entry(self.Frame3)
        self.Entry3.place(relx=0.07, rely=0.323,height=21, relwidth=0.201)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(textvariable=GUI_phase_support.eq_te)

        self.Entry4 = Entry(self.Frame3)
        self.Entry4.place(relx=0.07, rely=0.473,height=21, relwidth=0.201)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(textvariable=GUI_phase_support.eq_ph)

        self.Frame1 = Frame(self.Frame3)
        self.Frame1.place(relx=0.422, rely=0.129, relheight=0.849
                , relwidth=0.548)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=545)

        self.Entry5 = Entry(self.Frame3)
        self.Entry5.place(relx=0.281, rely=0.667,height=21, relwidth=0.086)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(textvariable=GUI_phase_support.st_de)

        self.Label7 = Label(self.Frame3)
        self.Label7.place(relx=0.02, rely=0.667, height=21, width=114)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(borderwidth="2")
        self.Label7.configure(text='''number of points:''')

        self.point_num_entry = Entry(self.Frame3)
        self.point_num_entry.place(relx=0.141, rely=0.667, height=21
                , relwidth=0.076)
        self.point_num_entry.configure(background="white")
        self.point_num_entry.configure(font="TkFixedFont")
        self.point_num_entry.configure(selectbackground="#c4c4c4")
        self.point_num_entry.configure(textvariable=GUI_phase_support.point_num)

        self.Button2 = Button(self.Frame3)
        self.Button2.place(relx=0.151, rely=0.763, height=34, width=69)
        self.Button2.configure(activebackground="#d9d9d9")
        self._img2 = PhotoImage(file="./upload_button.png")
        self.Button2.configure(image=self._img2)
        self.Button2.configure(text='''Button''')
        self.Button2.bind('<Button-1>',lambda e:GUI_phase_support.LoadSim_pressed(e))

        self.Checkbutton5 = Checkbutton(self.Frame3)
        self.Checkbutton5.place(relx=0.02, rely=0.237, relheight=0.045
                , relwidth=0.124)
        self.Checkbutton5.configure(activebackground="#d9d9d9")
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='''Add Rand Noise''')
        self.Checkbutton5.configure(variable=GUI_phase_support.ck_rand_de)

        self.Checkbutton6 = Checkbutton(self.Frame3)
        self.Checkbutton6.place(relx=0.015, rely=0.387, relheight=0.045
                , relwidth=0.134)
        self.Checkbutton6.configure(activebackground="#d9d9d9")
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='''Add Rand Noise''')
        self.Checkbutton6.configure(variable=GUI_phase_support.ck_rand_te)

        self.Entry13 = Entry(self.Frame3)
        self.Entry13.place(relx=0.151, rely=0.387,height=21, relwidth=0.147)
        self.Entry13.configure(background="white")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(selectbackground="#c4c4c4")
        self.Entry13.configure(textvariable=GUI_phase_support.rand_te)

        self.Checkbutton7 = Checkbutton(self.Frame3)
        self.Checkbutton7.place(relx=0.02, rely=0.538, relheight=0.045
                , relwidth=0.124)
        self.Checkbutton7.configure(activebackground="#d9d9d9")
        self.Checkbutton7.configure(justify=LEFT)
        self.Checkbutton7.configure(text='''Add Rand Noise''')
        self.Checkbutton7.configure(variable=GUI_phase_support.ck_rand_ph)

        self.Entry14 = Entry(self.Frame3)
        self.Entry14.place(relx=0.151, rely=0.538,height=21, relwidth=0.147)
        self.Entry14.configure(background="white")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(selectbackground="#c4c4c4")
        self.Entry14.configure(textvariable=GUI_phase_support.rand_ph)

        self.Label18 = Label(self.Frame3)
        self.Label18.place(relx=0.302, rely=0.237, height=19, width=104)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(text='''(rad^2/Hz)@1Hz''')

        self.Label18 = Label(self.Frame3)
        self.Label18.place(relx=0.302, rely=0.387, height=19, width=104)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(text='''(rad^2/Hz)@1Hz''')

        self.Label18 = Label(self.Frame3)
        self.Label18.place(relx=0.302, rely=0.538, height=19, width=104)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(text='''(rad^2/Hz)@1Hz''')

        self.Label19 = Label(self.Frame3)
        self.Label19.place(relx=0.236, rely=0.667, height=19, width=44)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(text='''Tsamp''')

        self.Label20 = Label(self.Frame3)
        self.Label20.place(relx=0.377, rely=0.667, height=19, width=18)
        self.Label20.configure(activebackground="#f9f9f9")
        self.Label20.configure(text='''(s)''')

        self.Button8 = Button(self.Frame3)
        self.Button8.place(relx=0.302, rely=0.882, height=37, width=87)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(text='''PHI PSD''')
        self.Button8.bind('<Button-1>',lambda e:GUI_phase_support.phipsd_pressed(e))

        self.Entry15 = Entry(self.Frame3)
        self.Entry15.place(relx=0.151, rely=0.237,height=21, relwidth=0.147)
        self.Entry15.configure(background="white")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(selectbackground="#c4c4c4")
        self.Entry15.configure(textvariable=GUI_phase_support.rand_de)

        self.Frame4 = Frame(self.TNotebook1_t1)
        self.Frame4.place(relx=0.015, rely=0.117, relheight=0.425
                , relwidth=0.482)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(width=650)

        self.Frame5 = Frame(self.TNotebook1_t1)
        self.Frame5.place(relx=0.497, rely=0.117, relheight=0.425
                , relwidth=0.482)
        self.Frame5.configure(relief=GROOVE)
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief=GROOVE)
        self.Frame5.configure(width=650)

        self.Frame6 = Frame(self.TNotebook1_t1)
        self.Frame6.place(relx=0.015, rely=0.543, relheight=0.425
                , relwidth=0.482)
        self.Frame6.configure(relief=GROOVE)
        self.Frame6.configure(borderwidth="2")
        self.Frame6.configure(relief=GROOVE)
        self.Frame6.configure(width=650)

        self.Frame7 = Frame(self.TNotebook1_t1)
        self.Frame7.place(relx=0.497, rely=0.543, relheight=0.425
                , relwidth=0.482)
        self.Frame7.configure(relief=GROOVE)
        self.Frame7.configure(borderwidth="2")
        self.Frame7.configure(relief=GROOVE)
        self.Frame7.configure(width=650)

        self.Button4 = Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.096, rely=0.015, height=27, width=82)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''REFRESH''')
        self.Button4.bind('<Button-1>',lambda e:GUI_phase_support.Refresh_pressed(e))

        self.Labelframe1 = LabelFrame(self.TNotebook1_t1)
        self.Labelframe1.place(relx=0.482, rely=0.007, relheight=0.095
                , relwidth=0.267)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Lowpass FIlter''')
        self.Labelframe1.configure(width=360)

        self.Entry9 = Entry(self.Labelframe1)
        self.Entry9.place(relx=0.306, rely=0.462, height=21, relwidth=0.267
                , bordermode='ignore')
        self.Entry9.configure(background="white")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(textvariable=GUI_phase_support.freq_cut)

        self.Label9 = Label(self.Labelframe1)
        self.Label9.place(relx=0.056, rely=0.462, height=19, width=57
                , bordermode='ignore')
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(borderwidth="2")
        self.Label9.configure(text='''Cut freq.:''')

        self.Checkbutton1 = Checkbutton(self.Labelframe1)
        self.Checkbutton1.place(relx=0.722, rely=0.462, relheight=0.323
                , relwidth=0.175, bordermode='ignore')
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Apply''')
        self.Checkbutton1.configure(variable=GUI_phase_support.applyfilt)

        self.Label12 = Label(self.Labelframe1)
        self.Label12.place(relx=0.611, rely=0.462, height=21, width=21
                , bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(borderwidth="2")
        self.Label12.configure(text='''Hz''')

        self.Label12 = Label(self.Labelframe1)
        self.Label12.place(relx=1.222, rely=0.308, height=19, width=19
                , bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(borderwidth="2")
        self.Label12.configure(text='''Hz''')

        self.Labelframe2 = LabelFrame(self.TNotebook1_t1)
        self.Labelframe2.place(relx=0.237, rely=0.007, relheight=0.095
                , relwidth=0.222)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(text='''Add white noise''')
        self.Labelframe2.configure(width=300)

        self.Entry11 = Entry(self.Labelframe2)
        self.Entry11.place(relx=0.2, rely=0.462, height=21, relwidth=0.32
                , bordermode='ignore')
        self.Entry11.configure(background="white")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(selectbackground="#c4c4c4")
        self.Entry11.configure(textvariable=GUI_phase_support.pow_value)

        self.Label13 = Label(self.Labelframe2)
        self.Label13.place(relx=0.033, rely=0.462, height=19, width=36
                , bordermode='ignore')
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(borderwidth="2")
        self.Label13.configure(text='''PSD:''')

        self.Label14 = Label(self.Labelframe2)
        self.Label14.place(relx=0.533, rely=0.462, height=19, width=59
                , bordermode='ignore')
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(borderwidth="2")
        self.Label14.configure(text='''(V^2/Hz)''')

        self.Checkbutton2 = Checkbutton(self.Labelframe2)
        self.Checkbutton2.place(relx=0.75, rely=0.462, relheight=0.323
                , relwidth=0.2, bordermode='ignore')
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Apply''')
        self.Checkbutton2.configure(variable=GUI_phase_support.applynoise)

        self.Entry10 = Entry(self.TNotebook1_t1)
        self.Entry10.place(relx=0.126, rely=0.073,height=21, relwidth=0.071)
        self.Entry10.configure(background="white")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(selectbackground="#c4c4c4")
        self.Entry10.configure(textvariable=GUI_phase_support.freq_samp)

        self.Label10 = Label(self.TNotebook1_t1)
        self.Label10.place(relx=0.052, rely=0.073, height=19, width=93)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(borderwidth="2")
        self.Label10.configure(text='''Sampling freq.:''')

        self.Label12 = Label(self.TNotebook1_t1)
        self.Label12.place(relx=0.2, rely=0.073, height=19, width=19)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(borderwidth="2")
        self.Label12.configure(text='''Hz''')

        self.Frame9 = Frame(self.TNotebook1_t2)
        self.Frame9.place(relx=0.497, rely=0.103, relheight=0.425
                , relwidth=0.482)
        self.Frame9.configure(relief=GROOVE)
        self.Frame9.configure(borderwidth="2")
        self.Frame9.configure(relief=GROOVE)
        self.Frame9.configure(width=650)

        self.Frame10 = Frame(self.TNotebook1_t2)
        self.Frame10.place(relx=0.015, rely=0.528, relheight=0.425
                , relwidth=0.482)
        self.Frame10.configure(relief=GROOVE)
        self.Frame10.configure(borderwidth="2")
        self.Frame10.configure(relief=GROOVE)
        self.Frame10.configure(width=650)

        self.Frame11 = Frame(self.TNotebook1_t2)
        self.Frame11.place(relx=0.497, rely=0.528, relheight=0.425
                , relwidth=0.482)
        self.Frame11.configure(relief=GROOVE)
        self.Frame11.configure(borderwidth="2")
        self.Frame11.configure(relief=GROOVE)
        self.Frame11.configure(width=650)

        self.Frame8 = Frame(self.TNotebook1_t2)
        self.Frame8.place(relx=0.015, rely=0.103, relheight=0.425
                , relwidth=0.482)
        self.Frame8.configure(relief=GROOVE)
        self.Frame8.configure(borderwidth="2")
        self.Frame8.configure(relief=GROOVE)
        self.Frame8.configure(width=650)

        self.Button5 = Button(self.TNotebook1_t2)
        self.Button5.place(relx=0.452, rely=0.015, height=47, width=77)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text='''REFRESH''')
        self.Button5.bind('<Button-1>',lambda e:GUI_phase_support.Refresh_PSD(e))

        self.Frame12 = Frame(self.TNotebook1_t3)
        self.Frame12.place(relx=0.007, rely=0.271, relheight=0.521, relwidth=0.4)

        self.Frame12.configure(relief=GROOVE)
        self.Frame12.configure(borderwidth="2")
        self.Frame12.configure(relief=GROOVE)
        self.Frame12.configure(width=540)

        self.Frame13 = Frame(self.TNotebook1_t3)
        self.Frame13.place(relx=0.423, rely=0.0, relheight=0.535, relwidth=0.437)

        self.Frame13.configure(relief=GROOVE)
        self.Frame13.configure(borderwidth="2")
        self.Frame13.configure(relief=GROOVE)
        self.Frame13.configure(width=590)

        self.Button6 = Button(self.TNotebook1_t3)
        self.Button6.place(relx=0.044, rely=0.117, height=47, width=97)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(text='''TRACK''')
        self.Button6.bind('<Button-1>',lambda e:GUI_phase_support.track_start(e))

        self.Label16 = Label(self.TNotebook1_t3)
        self.Label16.place(relx=0.141, rely=0.132, height=29, width=76)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(font=font9)
        self.Label16.configure(textvariable=GUI_phase_support.check_track)

        self.Button7 = Button(self.TNotebook1_t3)
        self.Button7.place(relx=0.319, rely=0.103, height=47, width=87)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(text='''PSD''')
        self.Button7.bind('<Button-1>',lambda e:GUI_phase_support.psd_phi(e))

        self.Frame14 = Frame(self.TNotebook1_t3)
        self.Frame14.place(relx=0.46, rely=0.543, relheight=0.433
                , relwidth=0.371)
        self.Frame14.configure(relief=GROOVE)
        self.Frame14.configure(borderwidth="2")
        self.Frame14.configure(relief=GROOVE)
        self.Frame14.configure(width=500)

        self.Entry7 = Entry(self.TNotebook1_t3)
        self.Entry7.place(relx=0.259, rely=0.088,height=21, relwidth=0.037)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(textvariable=GUI_phase_support.in_de)

        self.Entry16 = Entry(self.TNotebook1_t3)
        self.Entry16.place(relx=0.259, rely=0.132,height=21, relwidth=0.037)
        self.Entry16.configure(background="white")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(selectbackground="#c4c4c4")
        self.Entry16.configure(textvariable=GUI_phase_support.in_te)

        self.Entry17 = Entry(self.TNotebook1_t3)
        self.Entry17.place(relx=0.259, rely=0.176,height=21, relwidth=0.037)
        self.Entry17.configure(background="white")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(selectbackground="#c4c4c4")
        self.Entry17.configure(textvariable=GUI_phase_support.in_ph)

        self.Label21 = Label(self.TNotebook1_t3)
        self.Label21.place(relx=0.237, rely=0.088, height=19, width=20)
        self.Label21.configure(activebackground="#f9f9f9")
        self.Label21.configure(text='''De''')

        self.Label22 = Label(self.TNotebook1_t3)
        self.Label22.place(relx=0.237, rely=0.044, height=19, width=76)
        self.Label22.configure(activebackground="#f9f9f9")
        self.Label22.configure(text='''Start point''')

        self.Label23 = Label(self.TNotebook1_t3)
        self.Label23.place(relx=0.237, rely=0.132, height=19, width=18)
        self.Label23.configure(activebackground="#f9f9f9")
        self.Label23.configure(text='''Te''')

        self.Label24 = Label(self.TNotebook1_t3)
        self.Label24.place(relx=0.237, rely=0.176, height=21, width=19)
        self.Label24.configure(activebackground="#f9f9f9")
        self.Label24.configure(text='''Ph''')






if __name__ == '__main__':
    vp_start_gui()



