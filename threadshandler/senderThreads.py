from threadshandler.cfg import condition
from threading import Thread

class sender (Thread):


    def __init__(self, threadName):
        Thread.__init__(self)
        global sharedQueue
        self._args = ""
        self._threadName = threadName
        self._elementToSend = templateElement
        self._elementToSend['threadName'] = threadName


    def run(self):
        returnData = self.funcs[self.threadName](self.args)
        self.sendData(returnData)


    def sendData(self,listOfElements):

        # devo riempire elementToSend
        self._listToSend(listOfElements)


        condition.acquire()
        sharedQueue.put(self.elementToSend)
        condition.notify()
        condition.release()

    def _listToSend(self,listOfElements):
        self.elementToSend['Value'] = listOfElements

