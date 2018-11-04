#!/usr/bin/env python
#-*- CODING:UTF-8 -*-

#import sys
from tkinter import filedialog as fileDialog
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FCTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
#from matplotlib.figure import Figure
#from matplotlib.pyplot import figure
import phaseSimulation as phSim
import GUI.guiPhase as guiPhase
#from parser_sim import parse_function, parse_x
import numpy as np
import codecs
#import copy
#import PSD
#import datagenerator
import pathlib
#from configparser import ConfigParser
#from numpy import asarray as np_asarray
from threadshandler.senderThreads import tSender
from threading import Thread
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
from cfg import tkCfg, generalCfg as gCfg
from threadshandler.cfg import condition
import time

# Config files:
#CONFIG_PATH = pathlib.Path.cwd() / 'configFiles'
#LAST_ENTRY_NAME = 'last_entry.ini'

#last_entry_conf = ConfigParser()
#func_read = []
#samples = int()





def loadFile_clicked():
    print("loadFile clicked")

    ## check variables
    # contDelim
    # opFileName
    # contChunk
    # loMix
    # downSampling
    funcArgs = [tkCfg.contDelim, tkCfg.opFileName, tkCfg.contChunck, tkCfg.loMix, tkCfg.downSampling]
    if _allFilled([tkCfg.contDelim, tkCfg.opFileName, tkCfg.contChunck]):
        tkCfg.uploadCheck.set('Waiting...')
        loadFileT = tSender(name='loadFile', target=loadFile)
        loadFileT.start()
        tkCfg.uploadCheck.set('Done!')
    else:
        print('Error: need other values!')
    return

def loadSearch_clicked():
    guiPhase.generalGUI.changeProperty(tkCfg.app, element='loadSearchBtn', relief=tk.SUNKEN)
    fileSearched = fileDialog.askopenfilename(initialdir=gCfg.ROOT_PATH)
    if fileSearched:
        fileSearchedP = pathlib.Path(fileSearched).relative_to(gCfg.ROOT_PATH)
        tkCfg.opFileName.set(fileSearchedP)
        tkCfg.loadFileEntry.set(fileSearchedP)

    # Need to return "break" in order to release button after been sunken
    return "break"

def _allFilled(vars):
    allFilled = True
    for var in vars:
        if not var.get():
            allFilled = False
    return allFilled

########## THREADED FUNCTIONS ##########

def loadFile(*args, **kwargs):
    print("loadFile func")


    delDecoded = codecs.decode(tkCfg.contDelim.get(), 'unicode_escape') # decoded delimiter sign
    loadedData = np.array(phSim.loader(tkCfg.opFileName.get(),int(tkCfg.contChunck.get()),delDecoded))

    if tkCfg.loMix.get():
        loadedData[1:5]=phSim.downconvert(loadedData,float(tkCfg.freqLo.get()))

    if tkCfg.downSampling.get():
        loadedData=np.array(phSim.downsampl(loadedData,int(tkCfg.numDown.get())))

    tkCfg.dataDirLoad = 1
    tkCfg.isSim = 0
    return loadedData, tkCfg.dataDirLoad, tkCfg.isSim
