#!/usr/bin/env python
# -*- CODING:UTF-8 -*-

# import sys
import phaseSimulation as phSim
import GUI.guiPhase as guiPhase
import equationParser as eqParse
import numpy as np
import codecs
import pathlib
from threadshandler.senderThreads import TSender
import dataGen

try:
    import tkinter as tk
except ModuleNotFoundError:
    import Tkinter as tk

try:
    import tkinter.ttk as ttk
except ModuleNotFoundError:
    import ttk
from cfg import tkCfg, generalCfg as gCfg


def loadFile_clicked():
    # funcArgs = [tkCfg.contDelim, tkCfg.opFileName, tkCfg.contChunck, tkCfg.loMix, tkCfg.downSampling]
    if _allFilled([tkCfg.contDelim, tkCfg.opFileName, tkCfg.contChunck]):
        tkCfg.uploadCheck.set('Waiting...')
        loadFileT = TSender(name='loadFile', target=loadFile)
        loadFileT.start()
    else:
        print('Error: need other values!')
    return


def loadSearch_clicked():
    guiPhase.GeneralGUI.changeProperty(tkCfg.app, element='loadSearchBtn', relief=tk.SUNKEN)
    fileSearched = fileDialog.askopenfilename(initialdir=gCfg.ROOT_PATH)
    if fileSearched:
        fileSearchedP = pathlib.Path(fileSearched).relative_to(gCfg.ROOT_PATH)
        tkCfg.opFileName.set(fileSearchedP)
        tkCfg.loadFileEntry.set(fileSearchedP)

    # Need to return "break" in order to release button after been sunken
    return "break"


def on_LoadSim_pressed(event, btnObj):
    samples = int(tkCfg.pointNum.get())
    samplingTime = float(tkCfg.funcSamplTime.get())
    ckRands = [tkCfg.ckRands[i].get() for i in range(len(tkCfg.ckRands))]
    rands = [i.get() for i in tkCfg.rands]
    eqStr = [i.get() for i in tkCfg.equations]
    domData = eqParse.parseX(samplingTime, samples)
    funcs = eqParse.parseFuncs(eqStr)
    if not funcs:
        # Missing at least one of the three functions
        print('Missing functions...')
        return

    for index, ckStatus in enumerate(ckRands):
        print('Adding Noise')
        if ckStatus:
            if not rands[index] or rands[index].isalpha():
                print('Error: check rand entries...')
                funcs = None
                return
            addingRandom = dataGen.RandomWalk(float(rands[index]), 1/float(samplingTime))
            addingRandom.genRandom(samples)
            funcs[index] += addingRandom.getRandArray()

    eqStrName = ['eq_de', 'eq_te', 'eq_ph']

    for i in range(len(funcs)):
        # funcId = 'func-{}'.format(i + 1)
        btnObj.addPlot(eqStrName[i], domainList=domData, functionList=funcs[i])
    btnObj.showPlot()
    gCfg.loadedData = list(dataGen.dataGen(funcs))
    gCfg.loadedData.insert(0, np.zeros(samples))
    gCfg.loadedData = np.array(gCfg.loadedData)
    tkCfg.dataDirLoad = 1
    tkCfg.isSim = 1

    # write_last(func_read=func_read,times_read=times_read,samples=samples,rands=pow_list)


def _allFilled(passedVars):
    allFilled = True
    for var in passedVars:
        if not var.get():
            allFilled = False
    return allFilled


# ***** THREADED FUNCTIONS *****

def loadFile(*args, **kwargs):
    print("loadFile func")

    delDecoded = codecs.decode(tkCfg.contDelim.get(), 'unicode_escape')  # decoded delimiter sign
    loadedData = np.array(phSim.loader(tkCfg.opFileName.get(), int(tkCfg.contChunck.get()), delDecoded))

    if tkCfg.loMix.get():
        loadedData[1:5] = phSim.downconvert(loadedData, float(tkCfg.freqLo.get()))

    if tkCfg.downSampling.get():
        loadedData = np.array(phSim.downsampl(loadedData, int(tkCfg.numDown.get())))

    # I dont want to use queue so I just update values into the cfg files
    tkCfg.dataDirLoad = 1
    tkCfg.isSim = 0
    gCfg.loadedData = loadedData
    tkCfg.uploadCheck.set('Done!')
    return
