from threadshandler import cfg as tCfg
from threading import Thread
from cfg import generalCfg as gCfg, tkCfg


class TSender(Thread):
    def __init__(self, name=None, target=None, wantQueue=False, *args, **kwargs):
        super(TSender, self).__init__(name=name, target=target)
        self.threadName = str()
        self.threadName = name
        self._wantQueue = wantQueue
        self.daemon = True  # Kill thread when main is ended or killed
        self.func = target
        self.args = args
        self.kwargs = kwargs
        self._elementToSend = None
        return

    # Run override -> Comment this func and pass the function as target in kwargs
    # to the thread.__init__()

    def run(self):
        returnData = self.func(self.args, self.kwargs)
        self.sendData(returnData)
        return

    def sendData(self, *tupleToSend):
        # start gui polling

        self._elementToSend = tCfg.templateElement
        self._elementToSend['threadName'] = self.threadName
        self._elementToSend['Value'] = tupleToSend

        tCfg.condition.acquire()
        gCfg.sharedQueue.put(self._elementToSend)
        print('queueSend: {}'.format(gCfg.sharedQueue))
        tCfg.condition.notify()
        tCfg.condition.release()
        self._activeQueue()
        return

    def _activeQueue(self, *args, **kwargs):
        if self._wantQueue:
            tkCfg.app.receiveDataFromQueue.receiveData()
        return
