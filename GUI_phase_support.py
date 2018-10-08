#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 02, 2018 12:11:05 PM CEST  platform: Linux
#    Oct 02, 2018 02:31:35 PM CEST  platform: Linux
#    Oct 02, 2018 03:31:38 PM CEST  platform: Linux
#    Oct 02, 2018 03:33:26 PM CEST  platform: Linux
#    Oct 02, 2018 04:36:15 PM CEST  platform: Linux
#    Oct 03, 2018 10:46:20 AM CEST  platform: Linux
#    Oct 03, 2018 02:49:40 PM CEST  platform: Linux
#    Oct 03, 2018 02:53:50 PM CEST  platform: Linux
#    Oct 04, 2018 11:28:39 AM CEST  platform: Linux
#    Oct 04, 2018 11:59:27 AM CEST  platform: Linux
#    Oct 04, 2018 02:01:37 PM CEST  platform: Linux
#    Oct 04, 2018 03:55:43 PM CEST  platform: Linux
#    Oct 04, 2018 09:43:21 PM CEST  platform: Linux
#    Oct 05, 2018 03:16:45 PM CEST  platform: Linux
#    Oct 07, 2018 08:02:53 PM CEST  platform: Linux
#    Oct 08, 2018 11:31:23 AM CEST  platform: Linux

import sys
from tkinter import filedialog
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FCTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
import phase_sim
from parser_sim import parse_function, parse_x
from numpy import *
import codecs
import copy
import PSD
import pathlib
import configparser

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


# Config files:
CONFIG_PATH = pathlib.Path.cwd() / 'configFiles'
LAST_ENTRY_NAME = 'last_entry.ini'
# End Config files


def set_Tk_var():
    global contEntry1,filename
    contEntry1 = StringVar()
    filename=StringVar()
    sys.stdout.flush()
    global cont_delim
    cont_delim = StringVar()
    global cont_chunck
    cont_chunck = StringVar()
    global eq_de
    eq_de = StringVar()
    global eq_te
    eq_te = StringVar()
    global eq_ph
    eq_ph = StringVar()
    global st_de
    st_de = StringVar()
    global point_num
    point_num = StringVar()
    global freq_cut
    freq_cut = StringVar()
    global freq_samp
    freq_samp = StringVar()
    global applyfilt
    applyfilt = IntVar(0)
    global upload_check
    upload_check = StringVar()
    global pow_value
    pow_value = StringVar()
    global applynoise
    applynoise = IntVar()
    global dataorig
    dataorig=1
    global dataorig_f
    dataorig_f=1
    global noiseenter
    noiseenter=0
    global data_dir_load

    global lo_mix
    lo_mix = IntVar(0)
    global freq_lo
    freq_lo = StringVar()



def on_closing():
    print('GUI_phase_support.on_closing')
    #sys.stdout.flush()
    
    # Let's create LAST_ENTRY_NAME file:
    
    if not CONFIG_PATH.exists():
        CONFIG_PATH.mkdir()
        
    if not CONFIG_PATH / LAST_ENTRY_NAME).exists():
        create_last_entry()
    else:
        update_last_entry()
    
    destroy_window()

def create_last_entry():
    last_entry_conf = configparser.ConfigParser()
    
    last_entry_conf.add_section('EQUATIONS')
    last_entry_conf.add_section('SAMPLING_TIMES')
    last_entry_conf.add_section('N_SAMPLING')
        
    update_last_entry()

def update_last_entry():
    # Equations
    for i_eq in func_read:
        last_entry_conf.set('EQUATIONS','eq_' + str(i_eq+1), func_read[i])
    # Sampling times
        last_entry_conf.set('SAMPLING_TIMES', 'eq_' + str(i_eq+1), times_read[i])
    # Number of sampling
    last_entry_conf.set('N_SAMPLING', 'num', samples)
    last_entry_conf.write(CONFIG_PATH / LAST_ENTRY_NAME)
    
def read_last_entry():
    

def LoadSim_pressed(p1):
    global w
    
    samples = int(point_num.get())
    
    times_read = [st_de.get(), st_te.get(), st_ph.get()]
    times_read = list(map(int, times_read)) 
    
    func_read = [eq_de.get(), eq_te.get(), eq_ph.get()]
    
    #x_de = parse_x(st_de.get(), samples)
    #f_de = parse_function(eq_de.get(), x_de)
    #x_de= parse_x(st_de.get(), samples)
    #f_te = parse_function(eq_te.get(), x_de)
    #x_de= parse_x(st_de.get(), samples)
    #f_ph = parse_function(eq_ph.get(), x_de)
    
    last_x = parse_x(times_read,samples)
    last_func = parse_function(func_read)

    plots=array([np.asarray(last_func))
    plotrefresh(pl1[0],pl1[1],plots)

def Refresh_PSD(p1):
    global loaddata
    fs=float(freq_samp.get())
    psd1=PSD.plotpsd(loaddata[1],fs)
    plotrefresh(pl8[0],pl8[1],psd1[0],psd1[1],1)
    psd2=PSD.plotpsd(loaddata[2],fs)
    plotrefresh(pl9[0],pl9[1],psd2[0],psd2[1],1)
    psd3=PSD.plotpsd(loaddata[3],fs)
    plotrefresh(pl10[0],pl10[1],psd3[0],psd3[1],1)
    psd4=PSD.plotpsd(loaddata[4],fs)
    plotrefresh(pl11[0],pl11[1],psd4[0],psd4[1],1)


def LoadFile_pressed(e):
    global w,loaddata,upload_check,data_dir_load
    upload_check.set("Waiting...")
    w.Button3.config(relief=SUNKEN)
    del_decoded=codecs.decode(cont_delim.get(), 'unicode_escape')
    loaddata=array(phase_sim.loader(filename.get(),int(cont_chunck.get()),del_decoded))
    if lo_mix:
        loaddata[1:5]=phase_sim.downconvert(loaddata,float(freq_lo.get()))
    data_dir_load=1
    upload_check.set("Done!")
    #freq_samp.set(None)
    

    
def Refresh_pressed(p1):
    global loaddata,loaddataprev,dataorig,dataorig_f,noiseenter,data_dir_load
    
    if data_dir_load==0:
    
        try: 
            fss=float(freq_samp.get())
        
            if applynoise.get():
                noiseenter=1
                if dataorig:
                    loaddataprev=copy.copy(loaddata)
                loaddata[1:5]=phase_sim.whitenoise(loaddata[1:5],float(pow_value.get()),float(freq_samp.get()))
            else:
                try:    
                    loaddata=copy.copy(loaddataprev) 
                    dataorig=0
                    noiseenter=0
                except NameError:
                    print("noise not yet applied")
           
            try:
                fcc=float(freq_cut.get())
                if applyfilt.get():
                    if dataorig_f:
                        loaddataprev=copy.copy(loaddata)  
                    loaddata[1:5]=phase_sim.lowfilter(loaddata[1:5],fcc,fss)
     
                else:
                    try:  
                        if not(noiseenter):  
                            loaddata=copy.copy(loaddataprev) 
                            dataorig_f=0
                    except NameError:
                        print("filter not yet applied")   
            except ValueError:
                print("data fcut missing!")
                     
        except ValueError:
            print("data fsamp missing") 
            
    plotrefresh(pl4[0],pl4[1],loaddata[1])
    plotrefresh(pl5[0],pl5[1],loaddata[2])
    plotrefresh(pl6[0],pl6[1],loaddata[3])
    plotrefresh(pl7[0],pl7[1],loaddata[4])
    
    if data_dir_load==1:
        try:
            loaddataprev=copy.copy(loaddata)
        except NameError:
            print("first data load")
        data_dir_load=0

def Search_pressed(e):
    global filename
    name=filedialog.askopenfilename(initialdir=".")
    filename.set(name)
    w.Text1.insert(END,filename.get())
    sys.stdout.flush()
    

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    global pl1,pl4,pl5,pl6,pl7,pl8,pl9,pl10,pl11
    w = gui
    top_level = top
    root = top
    pl1=plotinit(w.Frame1)
    pl4=plotinit(w.Frame4)
    pl5=plotinit(w.Frame5)
    pl6=plotinit(w.Frame6)
    pl7=plotinit(w.Frame7)
    pl8=plotinit(w.Frame8)
    pl9=plotinit(w.Frame9)
    pl10=plotinit(w.Frame10)
    pl11=plotinit(w.Frame11)

def plotinit(framename):
    global w
    f1=framename
    f= Figure(figsize=(6, 4), dpi=100)  
    ax1= f.add_subplot(111)
    canvas= FCTkAgg(f, f1)
    toolbar = NavigationToolbar2Tk(canvas, f1 )
    toolbar.pack()
    canvas.get_tk_widget().pack()
    return ax1, canvas
    
def plotrefresh(ax, canvasobj,x,y=None,logactive=0):
    ax.clear()
    try:
        ax.plot(x,y)
    except ValueError:
        if len(x.shape)>1:
            for i in x:
                ax.plot(i)
        else:
            ax.plot(x)
    if logactive:
        ax.loglog()
    #xax=ax.get_xaxis().get_major_formatter()
        #xax.set_powerlimits((1,6))
        #xax.set_scientific(True)
    canvasobj.draw()
       
def destroy_window():
    # Function which closes the window.
    global top_level
    
    print("exiting")
    top_level.destroy()
    top_level = None
    


if __name__ == '__main__':
    import GUI_phase
    GUI_phase.vp_start_gui()















































































