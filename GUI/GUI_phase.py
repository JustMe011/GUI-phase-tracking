import tkinter as tk
import tkinter.ttk as ttk
import sys

IMG_PATH = "./img/"

class generalGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "GUI-phase-tracking")
        
        ########## STYLE ##########
        self.style = ttk.Style()
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Bitstream Vera Sans} -size 12 -weight normal"  \
            " -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        ########## Setting Notebook ##########
        self.top = ttk.Notebook(self)
        self.top.pack(side="top", fill="both", expand = True)
        self.top.place(relx=0.0, rely=0.014, relheight=1.0, relwidth=1.0)
        self.top.configure(width=300, takefocus="")
         
         
        tabs = {loadTab, secondTab}
        for Tab in tabs:
            tmpTab = Tab(self.top)
            self.top.add(tmpTab, text=tmpTab.tabName, padding=3)
            
        self.top.pack(expand=1, fill="both")
        self.top.update()
        
       
class templateTab(tk.Frame):
    def __init__(self, parent):
        self.currentTab = tk.Frame.__init__(self, parent)
        self.tabName = ""



class loadTab(templateTab, tk.Frame):
    def __init__(self, parent):
        templateTab.__init__(self, parent)
        self.tabName = "loadTab"

        
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
        #self.delimiterEntry.configure(textvariable=GUI_phase_support.cont_delim)
        
        self.loadFileBtn = tk.Button(self.loadTopFrame)
        self.loadFileBtn.place(relx=0.905, rely=0.261, height=34, width=69)
        self.loadBtnImg = tk.PhotoImage(file=IMG_PATH + "upload_button.png")
        self.loadFileBtn.configure(activebackground="#d9d9d9", image=self.loadBtnImg, text='''Button''')
        #self.loadFileBtn.bind('<Button-1>',lambda e:GUI_phase_support.LoadFile_pressed(e))
        
        self.chunckLbl = tk.Label(self.loadTopFrame)
        self.chunckLbl.place(relx=0.543, rely=0.609, height=19, width=50)
        self.chunckLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''Chunck:''')
        
        self.chunckEntry = tk.Entry(self.loadTopFrame)
        self.chunckEntry.place(relx=0.603, rely=0.609,height=21, relwidth=0.076)
        self.chunckEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.chunckEntry.configure(textvariable=GUI_phase_support.cont_chunck)
        
        self.uploadCheckLbl = tk.Label(self.loadTopFrame)
        self.uploadCheckLbl.place(relx=0.915, rely=0.609, height=19, width=36)
        self.uploadCheckLbl.configure(activebackground="#f9f9f9", borderwidth="2")
        #self.uploadCheckLbl.configure(textvariable=GUI_phase_support.upload_check)
        
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

        self.SamplTimeEntry = tk.Entry(self.insEqFrame)
        self.SamplTimeEntry.place(relx=0.281, rely=0.667,height=21, relwidth=0.086)
        self.SamplTimeEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.SamplTimeEntry.configure(textvariable=GUI_phase_support.st_de)

        self.pointNumLbl = tk.Label(self.insEqFrame)
        self.pointNumLbl.place(relx=0.02, rely=0.667, height=21, width=114)
        self.pointNumLbl.configure(activebackground="#f9f9f9", borderwidth="2", text='''number of points:''')

        self.pointNumEntry = tk.Entry(self.insEqFrame)
        self.pointNumEntry.place(relx=0.141, rely=0.667, height=21, relwidth=0.076)
        self.pointNumEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.pointNumEntry.configure(textvariable=GUI_phase_support.point_num)

        self.loadSimBtn = tk.Button(self.insEqFrame)
        self.loadSimBtn.place(relx=0.151, rely=0.763, height=34, width=69)
        self.loadSimBtn.configure(activebackground="#d9d9d9", image=self.loadBtnImg)
        #self.loadSimBtn.bind('<Button-1>',lambda e:GUI_phase_support.LoadSim_pressed(e))

        self.deAddNoiseCkBtn = tk.Checkbutton(self.insEqFrame)
        self.deAddNoiseCkBtn.place(relx=0.02, rely=0.237, relheight=0.045, relwidth=0.124)
        self.deAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.deAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_de)

        self.teAddNoiseCkBtn = tk.Checkbutton(self.insEqFrame)
        self.teAddNoiseCkBtn.place(relx=0.015, rely=0.387, relheight=0.045, relwidth=0.134)
        self.teAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.teAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_te)

        self.phAddNoiseCkBtn = tk.Checkbutton(self.insEqFrame)
        self.phAddNoiseCkBtn.place(relx=0.02, rely=0.538, relheight=0.045, relwidth=0.124)
        self.phAddNoiseCkBtn.configure(activebackground="#d9d9d9", justify=tk.LEFT, text='''Add Rand Noise''')
        #self.phAddNoiseCkBtn.configure(variable=GUI_phase_support.ck_rand_ph)

        self.deNoiseEntry = tk.Entry(self.insEqFrame)
        self.deNoiseEntry.place(relx=0.151, rely=0.237,height=21, relwidth=0.147)
        self.deNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.deNoiseEntry.configure(textvariable=GUI_phase_support.rand_de)
        
        self.teNoiseEntry = tk.Entry(self.insEqFrame)
        self.teNoiseEntry.place(relx=0.151, rely=0.387,height=21, relwidth=0.147)
        self.teNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.teNoiseEntry.configure(textvariable=GUI_phase_support.rand_te)

        self.phNoiseEntry = tk.Entry(self.insEqFrame)
        self.phNoiseEntry.place(relx=0.151, rely=0.538,height=21, relwidth=0.147)
        self.phNoiseEntry.configure(background="white", font="TkFixedFont", selectbackground="#c4c4c4")
        #self.phNoiseEntry.configure(textvariable=GUI_phase_support.rand_ph)

        self.freqDeLbl = tk.Label(self.insEqFrame)
        self.freqDeLbl.place(relx=0.302, rely=0.237, height=19, width=104)
        self.freqDeLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.freqTeLbl = tk.Label(self.insEqFrame)
        self.freqTeLbl.place(relx=0.302, rely=0.387, height=19, width=104)
        self.freqTeLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.freqPhLbl = tk.Label(self.insEqFrame)
        self.freqPhLbl.place(relx=0.302, rely=0.538, height=19, width=104)
        self.freqPhLbl.configure(activebackground="#f9f9f9", text='''(rad^2/Hz)@1Hz''')

        self.timeSampleLbl = tk.Label(self.insEqFrame)
        self.timeSampleLbl.place(relx=0.236, rely=0.667, height=19, width=44)
        self.timeSampleLbl.configure(activebackground="#f9f9f9", text='''Tsamp''')

        self.secondsLbl = tk.Label(self.insEqFrame)
        self.secondsLbl.place(relx=0.377, rely=0.667, height=19, width=18)
        self.secondsLbl.configure(activebackground="#f9f9f9", text='''(s)''')

        self.phiPsdBtn = tk.Button(self.insEqFrame)
        self.phiPsdBtn.place(relx=0.302, rely=0.882, height=37, width=87)
        self.phiPsdBtn.configure(activebackground="#d9d9d9", text='''PHI PSD''')
        #self.phiPsdBtn.bind('<Button-1>',lambda e:GUI_phase_support.phipsd_pressed(e))

        

        
        
class secondTab(templateTab, tk.Frame):
    def __init__(self, parent, tabName = ""):
        templateTab.__init__(self, parent)
        self.tabName = "secondTab"
        
