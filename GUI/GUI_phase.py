#!/usr/bin/env python
#-*- CODING:UTF-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import sys
import GUI.GUI_phase_support as GUI_phase_support
try:
    import queue
except:
    import Queue as queue
import pathlib
from cfg import tkCfg

IMG_PATH = str(pathlib.Path() / 'img') + "/"

class generalGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "GUI-phase-tracking")
        from cfg import tkCfg

        self.sharedQueue = queue.Queue()
        self.style = self._setStyle()
        self._tkVarsInit()

        ########## Setting Notebook ##########
        self.top = ttk.Notebook(self)
        self.top.pack(side="top", fill="both", expand = True)
        self.top.place(relx=0.0, rely=0.014, relheight=1.0, relwidth=1.0)
        self.top.configure(width=300, takefocus="")


        self.tabs = [loadTab, channelsTab, psdTab, recoveryTab]
        # For further uses
        # With getTabs() functions I can accesses from different tabs to each others
        self.tabsRefs = dict()

        for tabIndex in range(len(self.tabs)):
            tmpTab = self.tabs[tabIndex](self.top, self)
            #self.tabs[tabIndex] = tmpTab
            self.tabsRefs[self.tabs[tabIndex]] = tmpTab
            self.top.add(tmpTab, padding=3)
            self.top.tab(tabIndex, text=tmpTab.tabName,compound="left",underline="-1")
        self.top.pack(expand=1, fill="both")

    def _setStyle(self):
        ########## STYLE ##########
        style = ttk.Style()
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Bitstream Vera Sans} -size 12 -weight normal"  \
            " -slant roman -underline 0 -overstrike 0"
        style = ttk.Style()

        if sys.platform == "win32":
            style.theme_use('winnative')
        style.configure('.',background=_bgcolor)
        style.configure('.',foreground=_fgcolor)
        style.configure('.',font="TkDefaultFont")
        style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        return style

    def getTab(self, tabClass):
        # Return a reference to the controlled tab
        # Now, we're in the controller class
        return self.tabs[tabClass]

    def _tkVarsInit(self):
        tkCfg.opFileName = tk.StringVar()
        tkCfg.uploadCheck = tk.StringVar()
        tkCfg.contChunck = tk.StringVar()
        tkCfg.equations = [tk.StringVar() for i in range(3)]
        tkCfg.st_de = tk.StringVar()
        tkCfg.pointNum = tk.StringVar()
        tkCfg.cutOffFreq = tk.StringVar()
        tkCfg.samplingFreq = tk.StringVar()
        tkCfg.applyFilt = tk.IntVar(0)
        tkCfg.powVal = tk.StringVar()
        tkCfg.applyNoise =
        #tkCfg.dataDirLoad =
        #tkCfg.isSim =
        tkCfg.loMix = tk.IntVar(0)
        tkCfg.freqLo = tk.StringVar()
        tkCfg.checkTrack = tk.StringVar()
        tkCfg.downSampling = tk.IntVar(0)
        tkCfg.numDown = tk.StringVar()
        tkCfg.rands = [tk.StringVar() for i in range(3)]
        tkCfg.ckRands = [tk.StringVar() for i in range(3)]
        tkCfg.ins = [tk.StringVar() for i in range(3)]

class templateTab(tk.Frame):
    def __init__(self, parent, controller):
        self.currentTab = tk.Frame.__init__(self, parent)
        self.tabName = str()
        self.configure(background="#a8a8a8")
        self.controller = controller






class loadTab(templateTab, tk.Frame):
    def __init__(self, parent, controller):
        templateTab.__init__(self, parent, controller)
        self.tabName = "LOAD"



        self.loadTopFrame = tk.Frame(self)
        self.loadTopFrame.place(relx=0.126, rely=0.044, relheight=0.169
                , relwidth=0.738)
        self.loadTopFrame.configure(relief=tk.GROOVE, borderwidth="2", width=995)

        ## loadTopFrame ##
        self.loadFromFileLbl = tk.Label(self.loadTopFrame)
        self.loadFromFileLbl.place(relx=0.322, rely=0.087, height=29, width=251)
        self.loadFromFileLbl.configure(activebackground="#841216", activeforeground="white", background="#d8d582", borderwidth="2", justify=tk.RIGHT, relief=tk.SUNKEN, text='''Load from file''')

        self.loadSearchBtn = tk.Button(self.loadTopFrame)
        self.loadSearchBtn.place(relx=0.03, rely=0.609, height=27, width=68)
        self.loadSearchBtn.configure(activebackground="#d9d9d9", text='''Search''')
        #self.loadSearchBtn.bind('<Button-1>',lambda e:GUI_phase_support.Search_pressed(e))

        self.loadFromFileTxt = tk.Text(self.loadTopFrame)
        self.loadFromFileTxt.place(relx=0.121, rely=0.609, relheight=0.226, relwidth=0.257)
        self.loadFromFileTxt.configure(font="TkTextFont", selectbackground="#c4c4c4", width=256, wrap=tk.WORD)

        self.delimiterLlb = tk.Label(self.loadTopFrame)
        self.delimiterLlb.place(relx=0.402, rely=0.609, height=21, width=76)
        self.delimiterLlb.configure(activebackground="#f9f9f9", borderwidth="2", text='''Delimiter:''')

        self.delimiterEntry = tk.Entry(self.loadTopFrame)
        self.delimiterEntry.place(relx=0.482, rely=0.609,height=21, relwidth=0.036)
        self.delimiterEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.delimiterEntry.configure(textvariable=GUI_phase_support.elim)

        self.loadFileBtn = tk.Button(self.loadTopFrame)
        self.loadFileBtn.place(relx=0.905, rely=0.261, height=34, width=69)
        self.loadBtnImg = tk.PhotoImage(file=IMG_PATH + "upload_button.png")
        self.loadFileBtn.configure(activebackground="#d9d9d9", image=self.loadBtnImg, text='''Button''')
        self.loadFileBtn.bind('<Button-1>',lambda e:GUI_phase_support.loadFile_clicked())

        self.chunckLbl = tk.Label(self.loadTopFrame)
        self.chunckLbl.place(relx=0.543, rely=0.609, height=19, width=36)
        self.chunckLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Chunck:''')

        self.chunckEntry = tk.Entry(self.loadTopFrame)
        self.chunckEntry.place(relx=0.603, rely=0.609,height=21, relwidth=0.076)
        self.chunckEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.chunckEntry.configure(textvariable=self.controller.tkSharedVars['contChunck'])

        self.uploadCheckLbl = tk.Label(self.loadTopFrame)
        self.uploadCheckLbl.place(relx=0.915, rely=0.609, height=19, width=60)
        self.uploadCheckLbl.configure(activebackground="#f9f9f9", borderwidth="2")
        self.uploadCheckLbl.configure(textvariable=tkCfg.uploadCheck)



        self.loMixCkBtn = tk.Checkbutton(self.loadTopFrame)
        self.loMixCkBtn.place(relx=0.754, rely=0.087, relheight=0.183, relwidth=0.068)
        self.loMixCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''LO mix''')
        #self.loMixCkBtn.configure(variable=GUI_phase_support.lo_mix)

        self.freqLoEntry = tk.Entry(self.loadTopFrame)
        self.freqLoEntry.place(relx=0.709, rely=0.261,height=21, relwidth=0.117)
        self.freqLoEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.freqLoEntry.configure(textvariable=GUI_phase_support.freq_lo)

        self.hzLbl = tk.Label(self.loadTopFrame)
        self.hzLbl.place(relx=0.834, rely=0.261, height=19, width=19)
        self.hzLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Hz''')

        self.downSampCkBtn = tk.Checkbutton(self.loadTopFrame)
        self.downSampCkBtn.place(relx=0.754, rely=0.522, relheight=0.183, relwidth=0.093)
        self.downSampCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Downsamp''')
        #self.downSampCkBtn.configure(variable=GUI_phase_support.downsamp)

        self.numDownEntry = tk.Entry(self.loadTopFrame)
        self.numDownEntry.place(relx=0.749, rely=0.739,height=21, relwidth=0.036)
        self.numDownEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.numDownEntry.configure(textvariable=GUI_phase_support.num_down)

        self.numLbl = tk.Label(self.loadTopFrame)
        self.numLbl.place(relx=0.794, rely=0.696, height=19, width=32)
        self.numLbl.configure(activebackground="#f9f9f9", text='''num''')

        ## loadBottomFrame ##
        self.loadBottomFrame = tk.Frame(self)
        self.loadBottomFrame.place(relx=0.126, rely=0.235, relheight=0.682, relwidth=0.738)
        self.loadBottomFrame.configure(relief=tk.GROOVE, borderwidth="2", width=995)

        self.loadFromSimLbl = tk.Label(self.loadBottomFrame)
        self.loadFromSimLbl.place(relx=0.322, rely=0.043, height=29, width=251)
        self.loadFromSimLbl.configure(activebackground="#841216", activeforeground="white", background="#d8d582", borderwidth="2", justify=tk.RIGHT, relief=tk.SUNKEN, text='''Load from simulated data''')

        self.deLbl = tk.Label(self.loadBottomFrame)
        self.deLbl.place(relx=0.02, rely=0.161, height=21, width=23)
        self.deLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''DE''')

        self.teLbl = tk.Label(self.loadBottomFrame)
        self.teLbl.place(relx=0.02, rely=0.323, height=21, width=21)
        self.teLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''TE''')

        self.phLbl = tk.Label(self.loadBottomFrame)
        self.phLbl.place(relx=0.02, rely=0.473, height=21, width=22)
        self.phLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''PH''')

        self.deEntry = tk.Entry(self.loadBottomFrame)
        self.deEntry.place(relx=0.07, rely=0.172,height=21, relwidth=0.201)
        self.deEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.deEntry.configure(textvariable=GUI_phase_support.eq_de)

        self.teEntry = tk.Entry(self.loadBottomFrame)
        self.teEntry.place(relx=0.07, rely=0.323,height=21, relwidth=0.201)
        self.teEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.teEntry.configure(textvariable=GUI_phase_support.eq_te)

        self.phEntry = tk.Entry(self.loadBottomFrame)
        self.phEntry.place(relx=0.07, rely=0.473,height=21, relwidth=0.201)
        self.phEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.phEntry.configure(textvariable=GUI_phase_support.eq_ph)

        self.insEqFrame = tk.Frame(self.loadBottomFrame)
        self.insEqFrame.place(relx=0.422, rely=0.129, relheight=0.849, relwidth=0.548)
        self.insEqFrame.configure(relief=tk.GROOVE, borderwidth="2", width=545)

        self.SamplTimeEntry = tk.Entry(self.loadBottomFrame)
        self.SamplTimeEntry.place(relx=0.281, rely=0.667,height=21, relwidth=0.086)
        self.SamplTimeEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.SamplTimeEntry.configure(textvariable=GUI_phase_support.st_de)

        self.pointNumLbl = tk.Label(self.loadBottomFrame)
        self.pointNumLbl.place(relx=0.02, rely=0.667, height=21, width=114)
        self.pointNumLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''number of points:''')

        self.pointNumEntry = tk.Entry(self.loadBottomFrame)
        self.pointNumEntry.place(relx=0.141, rely=0.667, height=21, relwidth=0.076)
        self.pointNumEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.pointNumEntry.configure(textvariable=GUI_phase_support.point_num)

        self.loadSimBtn = tk.Button(self.loadBottomFrame)
        self.loadSimBtn.place(relx=0.151, rely=0.763, height=34, width=69)
        self.loadSimBtn.configure(activebackground="#d9d9d9", image=self.loadBtnImg)
        #self.loadSimBtn.bind('<Button-1>',lambda e:GUI_phase_support.LoadSim_pressed(e))

        self.deAddNoiseCkBtn = tk.Checkbutton(self.loadBottomFrame)
        self.deAddNoiseCkBtn.place(relx=0.02, rely=0.237, relheight=0.045, relwidth=0.124)
        self.deAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.deAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_de)

        self.teAddNoiseCkBtn = tk.Checkbutton(self.loadBottomFrame)
        self.teAddNoiseCkBtn.place(relx=0.015, rely=0.387, relheight=0.045, relwidth=0.134)
        self.teAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.teAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_te)

        self.phAddNoiseCkBtn = tk.Checkbutton(self.loadBottomFrame)
        self.phAddNoiseCkBtn.place(relx=0.02, rely=0.538, relheight=0.045, relwidth=0.124)
        self.phAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.phAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_ph)

        self.deNoiseEntry = tk.Entry(self.loadBottomFrame)
        self.deNoiseEntry.place(relx=0.151, rely=0.237,height=21, relwidth=0.147)
        self.deNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.deNoiseEntry.configure(textvariable=GUI_phase_support.rand_de)

        self.teNoiseEntry = tk.Entry(self.loadBottomFrame)
        self.teNoiseEntry.place(relx=0.151, rely=0.387,height=21, relwidth=0.147)
        self.teNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.teNoiseEntry.configure(textvariable=GUI_phase_support.rand_te)

        self.phNoiseEntry = tk.Entry(self.loadBottomFrame)
        self.phNoiseEntry.place(relx=0.151, rely=0.538,height=21, relwidth=0.147)
        self.phNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.phNoiseEntry.configure(textvariable=GUI_phase_support.rand_ph)

        self.freqDeLbl = tk.Label(self.loadBottomFrame)
        self.freqDeLbl.place(relx=0.302, rely=0.237, height=19, width=104)
        self.freqDeLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.freqTeLbl = tk.Label(self.loadBottomFrame)
        self.freqTeLbl.place(relx=0.302, rely=0.387, height=19, width=104)
        self.freqTeLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.freqPhLbl = tk.Label(self.loadBottomFrame)
        self.freqPhLbl.place(relx=0.302, rely=0.538, height=19, width=104)
        self.freqPhLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.timeSampleLbl = tk.Label(self.loadBottomFrame)
        self.timeSampleLbl.place(relx=0.236, rely=0.667, height=19, width=44)
        self.timeSampleLbl.configure(activebackground="#f9f9f9", text='''Tsamp''')

        self.secondsLbl = tk.Label(self.loadBottomFrame)
        self.secondsLbl.place(relx=0.377, rely=0.667, height=19, width=18)
        self.secondsLbl.configure(activebackground="#f9f9f9", text='''(s)''')

        self.phiPsdBtn = tk.Button(self.loadBottomFrame)
        self.phiPsdBtn.place(relx=0.302, rely=0.882, height=37, width=87)
        self.phiPsdBtn.configure(activebackground="#d9d9d9", text='''PHI PSD''')
        #self.phiPsdBtn.bind('<Button-1>',lambda e:GUI_phase_support.phipsd_pressed(e))


class channelsTab(templateTab, tk.Frame):
    def __init__(self, parent, controller):
        templateTab.__init__(self, parent, controller)
        self.tabName = "CHANNELS"

        self.charFirstFrame = tk.Frame(self)
        self.charFirstFrame.place(relx=0.015, rely=0.117, relheight=0.425, relwidth=0.482)
        self.charFirstFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.charSecondFrame = tk.Frame(self)
        self.charSecondFrame.place(relx=0.497, rely=0.117, relheight=0.425, relwidth=0.482)
        self.charSecondFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.charThirdFrame = tk.Frame(self)
        self.charThirdFrame.place(relx=0.015, rely=0.543, relheight=0.425, relwidth=0.482)
        self.charThirdFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.charFourthFrame = tk.Frame(self)
        self.charFourthFrame.place(relx=0.497, rely=0.543, relheight=0.425, relwidth=0.482)
        self.charFourthFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)



        self.refreshBtn = tk.Button(self)
        self.refreshBtn.place(relx=0.096, rely=0.015, height=27, width=82)
        self.refreshBtn.configure(activebackground="#d9d9d9", text='''REFRESH''')
        #self.refreshBtn.bind('<Button-1>',lambda e:GUI_phase_support.Refresh_pressed(e))

        ## loPassFiltLblFrame ##


        self.loPassFiltLblFrame = tk.LabelFrame(self)
        self.loPassFiltLblFrame.place(relx=0.482, rely=0.007, relheight=0.095, relwidth=0.267)
        self.loPassFiltLblFrame.configure(relief=tk.GROOVE, text='''Lowpass FIlter''', width=360)

        self.loPassFreqEntry = tk.Entry(self.loPassFiltLblFrame)
        self.loPassFreqEntry.place(relx=0.306, rely=0.462, height=21, relwidth=0.267
                , bordermode='ignore')
        self.loPassFreqEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.loPassFreqEntry.configure(textvariable=GUI_phase_support.freq_cut)

        self.cutFreqLbl = tk.Label(self.loPassFiltLblFrame)
        self.cutFreqLbl.place(relx=0.056, rely=0.462, height=19, width=57, bordermode='ignore')
        self.cutFreqLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Cut freq.:''')

        self.applyFiltCkBtn = tk.Checkbutton(self.loPassFiltLblFrame)
        self.applyFiltCkBtn.place(relx=0.722, rely=0.462, relheight=0.323, relwidth=0.175, bordermode='ignore')
        self.applyFiltCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Apply''')
        #self.applyCkBtn.configure(variable=GUI_phase_support.applyfilt)

        self.HzLbl = tk.Label(self.loPassFiltLblFrame)
        self.HzLbl.place(relx=0.611, rely=0.462, height=21, width=21, bordermode='ignore')
        self.HzLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Hz''')

        self.HzLbl2 = tk.Label(self.loPassFiltLblFrame)
        self.HzLbl2.place(relx=1.222, rely=0.308, height=19, width=19, bordermode='ignore')
        self.HzLbl2.configure(activebackground="#f9f9f9", borderwidth="2", text='''Hz''')

        ## addWhiteNoiseFrame ##


        self.addWhiteNoiseFrame = tk.LabelFrame(self)
        self.addWhiteNoiseFrame.place(relx=0.237, rely=0.007, relheight=0.095, relwidth=0.222)
        self.addWhiteNoiseFrame.configure(relief=tk.GROOVE, text='''Add white noise''', width=300)

        self.powValEntry = tk.Entry(self.addWhiteNoiseFrame)
        self.powValEntry.place(relx=0.2, rely=0.462, height=21, relwidth=0.32, bordermode='ignore')
        self.powValEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.powValEntry.configure(textvariable=GUI_phase_support.pow_value)

        self.psdLbl = tk.Label(self.addWhiteNoiseFrame)
        self.psdLbl.place(relx=0.033, rely=0.462, height=19, width=36, bordermode='ignore')
        self.psdLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''PSD:''')

        self.NoiseUnitLbl = tk.Label(self.addWhiteNoiseFrame)
        self.NoiseUnitLbl.place(relx=0.533, rely=0.462, height=19, width=59, bordermode='ignore')
        self.NoiseUnitLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''(V^2/Hz)''')

        self.applyWhiteNoise = tk.Checkbutton(self.addWhiteNoiseFrame)
        self.applyWhiteNoise.place(relx=0.75, rely=0.462, relheight=0.323, relwidth=0.2, bordermode='ignore')
        self.applyWhiteNoise.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Apply''')
        #self.applyWhiteNoise.configure(variable=GUI_phase_support.applynoise)

        self.samplFreqEntry = tk.Entry(self)
        self.samplFreqEntry.place(relx=0.126, rely=0.073,height=21, relwidth=0.071)
        self.samplFreqEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.samplFreqEntry.configure(textvariable=GUI_phase_support.freq_samp)

        self.samplFreqLbl = tk.Label(self)
        self.samplFreqLbl.place(relx=0.052, rely=0.073, height=19, width=93)
        self.samplFreqLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Sampling freq.:''')

        self.hzLbl3 = tk.Label(self)
        self.hzLbl3.place(relx=0.2, rely=0.073, height=19, width=19)
        self.hzLbl3.configure(activebackground="#f9f9f9", borderwidth="2", text='''Hz''')







class psdTab(templateTab, tk.Frame):
    def __init__(self, parent, controller):
        templateTab.__init__(self, parent, controller)
        self.tabName = "CHs PSD"

        self.psdFirstFrame = tk.Frame(self)
        self.psdFirstFrame.place(relx=0.497, rely=0.103, relheight=0.425, relwidth=0.482)
        self.psdFirstFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.psdSecondFrame = tk.Frame(self)
        self.psdSecondFrame.place(relx=0.015, rely=0.528, relheight=0.425, relwidth=0.482)
        self.psdSecondFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.psdThirdFrame = tk.Frame(self)
        self.psdThirdFrame.place(relx=0.497, rely=0.528, relheight=0.425, relwidth=0.482)
        self.psdThirdFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.psdFourthFrame = tk.Frame(self)
        self.psdFourthFrame.place(relx=0.015, rely=0.103, relheight=0.425, relwidth=0.482)
        self.psdFourthFrame.configure(relief=tk.GROOVE, borderwidth="2", width=650)

        self.psdRefreshBtn = tk.Button(self)
        self.psdRefreshBtn.place(relx=0.452, rely=0.015, height=47, width=77)
        self.psdRefreshBtn.configure(activebackground="#d9d9d9", text='''REFRESH''')
        #self.psdRefreshBtn.bind('<Button-1>',lambda e:GUI_phase_support.Refresh_PSD(e))







class recoveryTab(templateTab, tk.Frame):
    def __init__(self, parent, controller):
        templateTab.__init__(self, parent, controller)
        self.tabName = "RECOVERY"

        self.recFirstFrame = tk.Frame(self)
        self.recFirstFrame.place(relx=0.007, rely=0.271, relheight=0.521, relwidth=0.4)
        self.recFirstFrame.configure(relief=tk.GROOVE, borderwidth="2", width=540)

        self.recSecondFrame = tk.Frame(self)
        self.recSecondFrame.place(relx=0.423, rely=0.0, relheight=0.535, relwidth=0.437)
        self.recSecondFrame.configure(relief=tk.GROOVE, borderwidth="2", width=590)

        self.trackBtn = tk.Button(self)
        self.trackBtn.place(relx=0.044, rely=0.117, height=47, width=97)
        self.trackBtn.configure(activebackground="#d9d9d9", text='''TRACK''')
        #self.trackBtn.bind('<Button-1>',lambda e:GUI_phase_support.track_start(e))

        self.checkTrackLbl = tk.Label(self)
        self.checkTrackLbl.place(relx=0.141, rely=0.132, height=29, width=76)
        self.checkTrackLbl.configure(activebackground="#f9f9f9")
        #self.checkTrackLbl.configure(textvariable=GUI_phase_support.check_track)

        self.psdBtn = tk.Button(self)
        self.psdBtn.place(relx=0.319, rely=0.103, height=47, width=87)
        self.psdBtn.configure(activebackground="#d9d9d9", text='''PSD''')
        #self.psdBtn.bind('<Button-1>',lambda e:GUI_phase_support.psd_phi(e))

        self.recThirdFrame = tk.Frame(self)
        self.recThirdFrame.place(relx=0.46, rely=0.543, relheight=0.433, relwidth=0.371)
        self.recThirdFrame.configure(relief=tk.GROOVE, borderwidth="2", width=500)

        self.inDeBtn = tk.Entry(self)
        self.inDeBtn.place(relx=0.259, rely=0.088,height=21, relwidth=0.037)
        self.inDeBtn.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.inDeBtn.configure(textvariable=GUI_phase_support.in_de)

        self.inTeBtn = tk.Entry(self)
        self.inTeBtn.place(relx=0.259, rely=0.132,height=21, relwidth=0.037)
        self.inTeBtn.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.inTeBtn.configure(textvariable=GUI_phase_support.in_te)

        self.inPhBtn = tk.Entry(self)
        self.inPhBtn.place(relx=0.259, rely=0.176,height=21, relwidth=0.037)
        self.inPhBtn.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.inPhBtn.configure(textvariable=GUI_phase_support.in_ph)

        self.deLbl = tk.Label(self)
        self.deLbl.place(relx=0.237, rely=0.088, height=19, width=20)
        self.deLbl.configure(activebackground="#f9f9f9", text='''De''')

        self.startPointLbl = tk.Label(self)
        self.startPointLbl.place(relx=0.237, rely=0.044, height=19, width=76)
        self.startPointLbl.configure(activebackground="#f9f9f9", text='''Start point''')

        self.teLbl = tk.Label(self)
        self.teLbl.place(relx=0.237, rely=0.132, height=19, width=18)
        self.teLbl.configure(activebackground="#f9f9f9", text='''Te''')

        self.phLbl = tk.Label(self)
        self.phLbl.place(relx=0.237, rely=0.176, height=21, width=19)
        self.phLbl.configure(activebackground="#f9f9f9", text='''Ph''')

    '''
    def processIncoming(self):
        # This is the CONSUMER
        #Handle all messages currently in the queue, if any.
        while self.sharedQueue.qsize():
            try:
                msg = self.sharedQueue.get(0)
                # Check contents of message and do whatever is needed.

                print(msg)
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass
    '''
    
