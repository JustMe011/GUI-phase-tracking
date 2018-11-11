#!/usr/bin/env python
#  -*- CODING:UTF-8 -*-
import sys

# Check python version
try:
    assert sys.version_info >= (3, 0)
except AssertionError:
    print("Error: you should use Python3")
    exit(1)

import GUI.guiPhase as GUI

try:
    import queue
except ModuleNotFoundError:
    import Queue as queue
from cfg import tkCfg


def main():
    # Starting default thread -> GUI

    tkCfg.app = GUI.GeneralGUI()
    tkCfg.app.geometry("1351x706+-3+-8")
    tkCfg.app.mainloop()


if __name__ == '__main__':
    main()
