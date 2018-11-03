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
import numpy as npy
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
    tkCfg.uploadCheck.set('Waiting...')
    loadFileT = tSender(target=loadFile, name='loadFile')
    loadFileT.start()
    tkCfg.uploadCheck.set('Done!')

def loadSearch_clicked():
    print("loadSearchBtn pressed")

    fileSearched = fileDialog.askopenfilename(initialdir=gCfg.ROOT_PATH)
    fileSearchedP = pathlib.Path(fileSearched).relative_to(gCfg.ROOT_PATH)
    tkCfg.opFileName.set(fileSearchedP)
    tkCfg.loadFileEntry.set(fileSearchedP)
    guiPhase.loadTab.loadSearchBtn.configure(relief=tk.SUNKEN)




########## THREADED FUNCTIONS ##########

def loadFile():
    print("loadFile func")
    delDecoded = codecs.decode(tkCfg.contDelim.get(), 'unicode_escape') # decoded delimiter sign
    loadedData = npy.array(phSim.loader(tkCfg.opFileName.get(),int(tkCfg.contChunck.get()),delDecoded))
    print('loadedData')
    print(loadedData)

    if tkCfg.loMix.get():
        loadedData[1:5]=phSim.downconvert(loadedData,float(tkCfg.freqLo.get()))

    if tkCfg.downSampling.get():
        loadedData=npy.array(phSim.downsampl(loadedData,int(tkCfg.numDown.get())))

    tkCfg.dataDirLoad = 1
    tkCfg.isSim = 0
    return loadedData, tkCfg.dataDirLoad, tkCfg.isSim

