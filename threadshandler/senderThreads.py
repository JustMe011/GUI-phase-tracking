from threadshandler import cfg as tCfg
from threading import Thread
from cfg import generalCfg as gCfg, tkCfg


class tSender (Thread):
    def __init__(self, name=None, target=None, *args, **kwargs):
        self.threadName = str()
        self.threadName = name

        super(tSender, self).__init__(name=self.threadName, target=target)
        self.daemon = True



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
        # start gui polling

        self._elementToSend = tCfg.templateElement
        self._elementToSend['threadName'] = self.threadName
        self._elementToSend['Value'] = tupleToSend

        tCfg.condition.acquire()
        gCfg.sharedQueue.put(self._elementToSend)
        print('queueSend: {}'.format(gCfg.sharedQueue))
        tCfg.condition.notify()
        tCfg.condition.release()
        tkCfg.app.receiveDataFromQueue.receiveData()

        return


