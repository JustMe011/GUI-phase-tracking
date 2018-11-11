# import matplotlib.pyplot as plt

import matplotlib
import matplotlib.style as mplstyle
from matplotlib.figure import Figure
import tkinter as tk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
mplstyle.use("bmh")


# Create the figure
class CreatePlot(object):
    def __init__(self, masterframe, figureSizeListPx, figdpi=100, **kwargs):
        # Create figure and axes...
        self.dpi = figdpi
        self.figureSize = self._toTuple(figureSizeListPx)
        self.fig = Figure(figsize=figureSizeListPx, dpi=self.dpi, constrained_layout=False)
        self.masterFrame = masterframe
        self.ax = self.fig.add_subplot(111)
        self.plots = []
        self.plotsName = []
        self.canvas = None
        self.toolbar = None

    def addPlot(self, funcId, domainList, functionList):
        if funcId in self.plotsName:
            self.updatePlot(funcId, domainList, functionList)
        else:
            if len(domainList) == len(functionList) and funcId:
                self.plots.append(self.ax.plot(domainList, functionList))
                self.plotsName.append(funcId)

    def showPlot(self, wantBar=True):
        # Create drawing area
        if not self.canvas:
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.masterFrame)

            if wantBar:
                self.toolbar = NavigationToolbar2Tk(self.canvas, self.masterFrame)
                # self.toolbar = _customToolbar(plotCanvas=self.canvas, frame=self.masterFrame)
                self.toolbar.update()
                self.toolbar.pack()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

        self.canvas.draw()

    def updatePlot(self, funcId, newX, newY):
        currIndex = self.plotsName.index(funcId)
        self.plots[currIndex][0].set_xdata(newX)
        self.plots[currIndex][0].set_ydata(newY)

        self.showPlot()

    def _toTuple(self, figSizePx):
        try:
            assert list == type(figSizePx)
        except AssertionError as e:
            e.args += ('figureSizeList is not a list', 42)
            raise
        # figsize should be a type of (width, height)
        figSize = self._pxToInch(figSizePx)
        return tuple(figSize)

    def _pxToInch(self, figureSizePx):
        inches = []
        for dim in figureSizePx:
            tmp = dim / self.dpi
            inches.append(round(tmp, 2))
        return inches


'''
    Future implementations -> create a custom toolbar with custom items
    with custom preferences, bindings, ...

    remember to add:
    self.toolbar = _customToolbar(plotCanvas=self.canvas, frame=self.masterFrame)
    during toolbar creation instead of the default constructor

class _customToolbar (NavigationToolbar2Tk):
    def __init__ (self, plotCanvas, frame, *buttons):
        # initialize toolbar object
        defaultItems =

        # Now I try to delete home btn
        #self.toolitems = filter(lambda x: x[0] != 'Subplots', NavigationToolbar2Tk.toolitems)
        #self.toolitems = (('Home', 'Lorem ipsum dolor sit amet', 'home', 'home'),(None,None,None,None))
        NavigationToolbar2Tk.__init__(self, plotCanvas, frame)

        self.iconDir =


#class _newItem

'''
