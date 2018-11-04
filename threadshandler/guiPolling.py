from threading import Thread, Lock
import threadshandler.cfg as cfg
from cfg import generalCfg as gCfg, tkCfg
import time

class guiPolling:
    def __init__(self):
        self._elToReceive = cfg.templateElement
        self._polRunning = True


    def receiveData(self):
        #print('polRunning: {}'.format(self._polRunning))
        #print('queue: {}'.format(gCfg.sharedQueue))
        while self._polRunning:
            time.sleep(1)
            if not gCfg.sharedQueue.empty():
                print('guiPolling')
                cfg.condition.acquire()
                self._elToReceive = gCfg.sharedQueue.get(0)
                print("receivedData")
                [print(self._elToReceive[i]) for i in list(self._elToReceive.keys())]
                cfg.condition.release()
                self._endPolling()
            else:
                print("empty queue")
                tkCfg.app.after(100,self.receiveData())
    def _endPolling(self):
        self._polRunning = False
