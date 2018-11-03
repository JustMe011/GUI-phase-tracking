from threadshandler import cfg as tCfg
from threading import Thread
from cfg import generalCfg as gCfg


class tSender (Thread):
    def __init__(self, name=None, target=None):
        self.threadName = str()
        self.threadName = name
        super(tSender, self).__init__(name=self.threadName, target=target)
        #self.funcArgs = funcArgs

        self._elementToSend = tCfg.templateElement
        self._elementToSend['threadName'] = self.threadName
        self.func = target
        return

     # Run override -> I could comment this func and pass the function as target in kwargs
    # to the thread.__init__()

    def run(self):
        self.func()
        return

    def sendData(self,*tupleToSend):
        tuple(listToSend)
        self.elementToSend['Value'] = tupleToSend

        tkCfg.condition.acquire()
        gCfg.sharedQueue.put(self.elementToSend)
        tCfg.condition.notify()
        tCfg.condition.release()
        return


