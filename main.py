#!/usr/bin/env python
#-*- CODING:UTF-8 -*-
import sys
# Check python version
try:
    assert sys.version_info >= (3,0)
except:
    print("Error: you should use Python3")
    exit(1)
    
import tkinter as tk
import GUI.guiPhase as GUI

try:
    import queue
except:
    import Queue as queue

def main():
    # Starting default thread -> GUI

    app = GUI.generalGUI()
    app.geometry("1351x706+-3+-8")
    
    app.after(100, app.receiveDataFromQueue())
    app.mainloop()


if __name__ == '__main__':
    main()
