

class sender (Thread):
    
    
    def __init__(self, threadName, *args):
        Thread.__init__(self)
        global sharedQueue
        print("args =" + str(args))
        self.args = args
        self.threadName = threadName
        self.elementToSend = templateElement
        self.elementToSend['threadName'] = threadName
        self.funcs = {"loadFile":self.loadFile}
    
    def run(self):
        returnData = self.funcs[self.threadName](self.args)
        self.sendData(returnData)
        
            
    def sendData(self,listOfElements):

        # devo riempire elementToSend
        self.listToSend(listOfElements)
        
        
        condition.acquire()
        sharedQueue.put(self.elementToSend)
        condition.notify()
        condition.release()
    
    def listToSend(self,listOfElements):
        self.elementToSend['Value'] = listOfElements
    
    def loadFile(self, *args):
        print("loadfile work")
        return []
