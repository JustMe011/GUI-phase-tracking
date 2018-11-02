from threadshandler import cfg as tCfg
from threading import Thread
from cfg import generalCfg as gCfg


class tSender (Thread):
    def __init__(self, threadName):
        Thread.__init__(self)
        self._args = str()
        self._threadName = threadName
        self._elementToSend = tCfg.templateElement
        self._elementToSend['threadName'] = threadName


    # def run(self):
    #     returnData = self.funcs[self.threadName](self.args)
    #     self.sendData(returnData)


    def sendData(self,listOfElements):

        # devo riempire elementToSend
        self._listToSend(listOfElements)


        tkCfg.condition.acquire()
        gCfg.sharedQueue.put(self.elementToSend)
        tCfg.condition.notify()
        tCfg.condition.release()

    def _listToSend(self,listOfElements):
        self.elementToSend['Value'] = listOfElements

