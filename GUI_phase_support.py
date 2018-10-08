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
#    Oct 07, 2018 11:56:10 PM CEST  platform: Linux
#    Oct 08, 2018 10:57:13 AM CEST  platform: Linux
#    Oct 08, 2018 01:57:02 PM CEST  platform: Linux
#    Oct 08, 2018 03:31:30 PM CEST  platform: Linux

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
import datagenerator

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
    global check_track
    check_track = StringVar()
    global downsamp
    downsamp = IntVar(0)
    global num_down
    num_down = StringVar()




def psd_phi(p1):
    fs=float(freq_samp.get())
    psd13=PSD.plotpsd(phil,fs)
    plotrefresh(pl13[0],pl13[1],psd13[0],psd13[1],1)
    
def track_start(p1):
    global loaddata,phil
    check_track.set("Wait...")
    dell,thel,phil=phase_sim.tracker(loaddata)
    tot=array([dell,thel,phil])
    plotrefresh(pl12[0],pl12[1],tot,col=["red","orange","green"])
    check_track.set("Done...")
    
def LoadSim_pressed(p1):
    global w,loaddata,data_dir_load
    
    samples = int(point_num.get())
    
    x_de = parse_x(st_de.get(), samples)
    f_de = parse_function(eq_de.get(), x_de)
    x_de= parse_x(st_de.get(), samples)
    f_te = parse_function(eq_te.get(), x_de)
    x_de= parse_x(st_de.get(), samples)
    f_ph = parse_function(eq_ph.get(), x_de)

    plots=array([f_de,f_te,f_ph])
    plotrefresh(pl1[0],pl1[1],plots,col=['r',"orange","green"])
    loaddata=list(datagenerator.datagen(f_de,f_te,f_ph))
    loaddata.insert(0,zeros(samples))
    data_dir_load=1

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
    
    
    if lo_mix.get():
        loaddata[1:5]=phase_sim.downconvert(loaddata,float(freq_lo.get()))
    if downsamp.get():
        loaddata=array(phase_sim.downsampl(loaddata,int(num_down.get())))
    data_dir_load=1
    upload_check.set("Done!")

    

    
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
    global pl1,pl4,pl5,pl6,pl7,pl8,pl9,pl10,pl11,pl12,pl13
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
    pl12=plotinit(w.Frame12)
    pl13=plotinit(w.Frame13)

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
    
def plotrefresh(ax, canvasobj,x,y=None,logactive=0,col='b'):
    ax.clear()
    try:
        ax.plot(x,y)
    except ValueError:
        if len(x.shape)>1:
            for n,i in enumerate(x):
                ax.plot(i,col[n])
        else:
            ax.plot(x,color=col)
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




























































































