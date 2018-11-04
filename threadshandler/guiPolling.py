from threading import Thread, Lock
import threadshandler.cfg as cfg
from cfg import generalCfg as gCfg
from cfg.tkCfg import tkGuiClass

class guiPolling:
    def __init__(self):
        self._elToReceive = cfg.templateElement
        self._polRunning = False

    def receiveData(self):
        while self._polRunning:
            if not gCfg.sharedQueue.empty():
                cfg.condition.acquire()
                self._elToReceive = gCfg.sharedQueue.get(0)
                print("receivedData")
                [print(self._elToReceive[i]) for i in list(self._elToReceive.keys())]
                cfg.condition.release()
                self._endPolling()
            else:
                print("empty queue")
                self.receiveData()
    def _endPolling(self):
        self._polRunning = False
