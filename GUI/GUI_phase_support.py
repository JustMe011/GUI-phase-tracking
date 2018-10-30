#!/usr/bin/env python
#-*- CODING:UTF-8 -*-

import sys
from tkinter import filedialog
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FCTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import figure
import phase_sim
from parser_sim import parse_function, parse_x
from numpy import *
import codecs
import copy
import PSD
import datagenerator
import pathlib
from configparser import ConfigParser
from numpy import asarray as np_asarray

try:
    import tkinter as tk
except:
    import Tkinter as tk

try:
    import tkinter.ttk as ttk
except:
    import ttk
from tkinter import messagebox
import threading

# Config files:
CONFIG_PATH = pathlib.Path.cwd() / 'configFiles'
LAST_ENTRY_NAME = 'last_entry.ini'

last_entry_conf = ConfigParser()
func_read = []
samples = int()

def set_Tk_var():
    
    global  contDelim = StringVar(),
    contChunck = StringVar(),
    equations[] = [StringVar()for i in range(3)],
    st_de = StringVar(),
    point_num = StringVar(),
    freqCut = StringVar(),
    SamplFreq = StringVar(),
    applyFilt = IntVar(0),
    uploadCheck = StringVar(),
    powValue = StringVar(),
    applyNoise = IntVar(),
    dataorig=1,
    dataorig_f=1,
    noiseenter=0,
    filtenter=0,
    data_dir_load,
    issim,
    loMix = IntVar(0),
    freqLo = StringVar(),
    checkTrack = StringVar(),
    downSamp = IntVar(0),
    numDown = StringVar(),
    rand[] = [StringVar() for i in range(3)],
    ckRand[] = [IntVar(0) for i in range(3)],
    in[] = [StringVar() for i in range(3)]
    
    
    
    
def loadFile_clicked():
    global w,filename
    
    uploadCheck.set("Waiting...")
    w.loadFileBtn.config(relief=tk.SUNKEN)
    loadFileThread = threadsHandler.createThread(self,loadFile,"loadFile",True)
    uploadCheck.set("Done!")
    
    # writelast function
    
def loadFile():
    delDecoded=codecs.decode(contDelim.get(), 'unicode_escape')
    loadData=array(phase_sim.loader(filename.get(),int(contChunck.get()),delDecoded))


    if lo_mix.get():
        loaddata[1:5]=phase_sim.downconvert(loaddata,float(freq_lo.get()))
    if downsamp.get():
        loaddata=array(phase_sim.downsampl(loaddata,int(num_down.get())))
    data_dir_load=1
    
    issim=0












