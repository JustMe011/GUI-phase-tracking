#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import GUI
import threading
try:
    import queue
except:
    import Queue as queue

class threadsHandler:

    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        # Class properties:
        self.master = master
        self.sharedQueue = queue.Queue()
        self.running = 1
        self.threadList = list()


        # START GUI -> MAIN THREAD
        self.mainWindow = GUI.generalGui(master, self.sharedQueue, self.endApplication)

        # Start the periodic call in the GUI to check if the queue contains anything
        self.pollingSharedQueue()



    def pollingSharedQueue(self):

        # POLLING QUEUE
        #Check every 200 ms if there is something new in the queue.

        GUI.generalGui.processIncoming(self)
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.pollingSharedQueue)


    def createThread(self, targetFunction, name, isDaemon):
        tmpThread = threading.Thread(target=targetFunction)
        tmpThread.setDaemon(isDaemon)
        tmpThread.setName(name)
        tmpThread.start()
        return tmpThread

    def endApplication(self):
        self.running = 0

