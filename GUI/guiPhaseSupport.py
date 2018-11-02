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
import phaseSimulation as phSim
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
    loadFileT = guiEvents('loadFile')
    tkCfg.uploadCheck.set('Done!')



class guiEvents(tSender):
    def __init__(self, funcName, threadName = '', *args):
        self.threadName = str()
        self.funcName = funcName
        self.funcArgs = args
        # if not threadName:
        #     self.threadName = funcName.__name__
        # else:
        #     self.threadName = threadName
        self.threadName = funcName if not threadName else threadName
        print('threadName: {}\nfuncName: {}\n'.format(self.threadName, self.funcName))
        tSender.__init__(self, self.threadName)

        self._runFunc()

    def _runFunc(self):
        returnData = getattr(self, self.funcName)(self.funcArgs)
        if 'NoneType' == type(returnData):
            returnData = tuple()
        print('returnData: {}'.format(returnData))
        #self.sendData(self, returnData)



    # def functions...
    def loadFile(self , *args):
        print("loadFile func")

        delDecoded = codecs.decode(tkCfg.contDelim.get(), 'unicode_escape') # decoded delimiter sign
        loadedData = npy.array(phSim.loader(tkCfg.opFileName.get(),int(tkCfg.contChunck.get()),delDecoded))

        if tkCfg.loMix.get():
        loadedData[1:5]=phSim.downconvert(loadedData,float(tkCfg.freqLo.get()))
        if tkCfg.downSampling.get():
            loadedData=npy.array(phSim.downsampl(loadedData,int(tkCfg.numDown.get())))
        tkCfg.dataDirLoad = 1
        tkCfg.isSim = 0
        return loadedData, tkCfg.dataDirLoad, tkCfg.isSim
