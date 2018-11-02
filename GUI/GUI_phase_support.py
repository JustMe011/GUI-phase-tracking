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
from threadshandler.senderThreads import tSender
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
    ## chiamera' qualcosa del tipo
    # loadFileT = guiEvents(loadFileCB, "loadFile")
    '''

    w.loadFileBtn.config(relief=tk.SUNKEN)

    uploadCheck.set("Done!")

    # writelast function
    '''



class guiEvents(tSender):
    def __init__(self, funcName, threadName = '', *args):
        self.threadName = str()
        # if not threadName:
        #     self.threadName = funcName.__name__
        # else:
        #     self.threadName = threadName
        self.threadName = funcName.__name__ if not threadName else threadName
        tSender.__init__(self, self.threadName, funcName)

        self._runFunc()

    def _runFunc(self):
        returnData = getattr(self, funcName)(args)
        self.sendData(self, returnData)



    # def functions...
    def loadFile():
        print("loadFile func")
