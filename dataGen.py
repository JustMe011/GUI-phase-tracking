
# ***** SIMULATOR OF THE OPTICAL FIBER *****


import numpy as np
import numpy.random as npr

# import matplotlib.colors
# import csv
# from mpl_toolkits.mplot3d import Axes3D
# import time

# *** fiber model: Jones calculation ***


def FibMod(delta, theta, phi):
    R1 = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    M = np.array([[np.e ** (1j * (-delta / 2)), 0], [0, np.e**(1j * (delta / 2))]])
    R2 = np.transpose(R1)
    Ein = np.array([np.cos(np.pi / 4) * np.e ** (1j * (np.pi / 2)), np.sin(np.pi / 4)]) * np.e ** (1j * phi)
    return R2.dot(M.dot(R1.dot(Ein)))

# ***** MAIN FUNCTION TO BE IMPORTED *****


def dataGen(funcArray):
   dearr, thearr, phiarr = funcArray

    t = []
    rex = []
    imx = []
    rey = []
    imy = []

    for i in np.arange(len(dearr)):
        dd = dearr[i]
        tt = thearr[i]
        pp = phiarr[i]

        Eout = FibMod(dd, tt, pp)
        Exr = Eout[0].real
        Exi = Eout[0].imag
        Eyr = Eout[1].real
        Eyi = Eout[1].imag
        rex.append(Exr)
        imx.append(Exi)
        rey.append(Eyr)
        imy.append(Eyi)

    # The order of the output is the same of the
    # Experimental setup real-imag-imag-real
    return np.array(rex), np.array(imx), np.array(imy), np.array(rey)

# Random walk generator


class RandomWalk:

    def __init__(self, pow1hz, fs):
        self._last = 0
        self._randLis = []
        self._ampli = np.sqrt(2 * np.pi * np.pi * pow1hz / fs)
        self._randElements = None

    def genRandom(self, t):
        for i in range(t):
            step = npr.normal(0, 1)
            self._last += step  # + (10**(-5))*npr.normal())
            self._randLis.append(self._last)
        self._randElements = np.array(self._randLis)
        self._randElements *= self._ampli

    def getRandArray(self):
        return self._randElements
