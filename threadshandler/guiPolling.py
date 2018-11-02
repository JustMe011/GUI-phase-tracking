from threading import Thread, Lock
import threadshandler.cfg as cfg
from cfg import generalCfg as gCfg

class guiPolling:
    def __init__(self):
        self._elToReceive = cfg.templateElement

    def receiveData(self):
        if not gCfg.sharedQueue.empty():
            cfg.condition.acquire()
            self._elToReceive = gCfg.sharedQueue.get(0)
            print("receivedData")
            [print(self._elToReceive[i]) for i in list(self._elToReceive.keys())]
            cfg.condition.release()
        else:
            print("empty queue")
