#!/usr/bin/env python
#-*- CODING:UTF-8 -*-

#import sys
#from tkinter import filedialog
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FCTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
#from matplotlib.figure import Figure
#from matplotlib.pyplot import figure
#import phase_sim
#from parser_sim import parse_function, parse_x
#import numpy as npy
#import codecs
#import copy
#import PSD
#import datagenerator
import pathlib
#from configparser import ConfigParser
#from numpy import asarray as np_asarray
#from threadshandler.senderThreads import sender
import time
try:
    import tkinter as tk
except:
    import Tkinter as tk

try:
    import tkinter.ttk as ttk
except:
    import ttk
#from tkinter import messagebox
#import threading
from cfg import tkCfg



# Config files:
#CONFIG_PATH = pathlib.Path.cwd() / 'configFiles'
#LAST_ENTRY_NAME = 'last_entry.ini'

#last_entry_conf = ConfigParser()
#func_read = []
#samples = int()





def loadFile_clicked():
    print("loadFile clicked")
    tkCfg.uploadCheck.set('Waiting...')

    #tkCfg.uploadCheck.set('Done!')
    '''

    w.loadFileBtn.config(relief=tk.SUNKEN)
    #loadFileThread = threadsHandler.createThread(self,loadFile,"loadFile",True)
    loadFileT = threadedFunctions("loadFile")
    uploadCheck.set("Done!")

    # writelast function
    '''






