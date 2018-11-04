from threadshandler import cfg as tCfg
from threading import Thread
from cfg import generalCfg as gCfg, tkCfg
from cfg.tkCfg import tkGuiClass

class tSender (Thread):
    def __init__(self, name=None, target=None, *args, **kwargs):
        self.threadName = str()
        self.threadName = name
        self.daemon = True
        super(tSender, self).__init__(name=self.threadName, target=target)

        # start gui polling
        tkGuiClass.receiveDataFromQueue.receiveData()

        self.func = target
        self.args = args
        self.kwargs = kwargs
        return

     # Run override -> I could comment this func and pass the function as target in kwargs
    # to the thread.__init__()

    def run(self):
        returnData = self.func(self.args, self.kwargs)
        self.sendData(returnData)
        return

    def sendData(self,*tupleToSend):
        print('sendData')
        print('tupleToSend')
        self._elementToSend = tCfg.templateElement
        self._elementToSend['threadName'] = self.threadName
        self._elementToSend['Value'] = tupleToSend
        print('toSend')
        print(self._elementToSend)

        tCfg.condition.acquire()
        gCfg.sharedQueue.put(self._elementToSend)
        tCfg.condition.notify()
        tCfg.condition.release()

        return


