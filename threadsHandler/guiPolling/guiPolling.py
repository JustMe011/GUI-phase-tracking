from threading import Thread, Lock, Condition


def receiveData():
    global sharedQueue
    elementToReceive = templateElement
    while True:
        condition.acquire()
        if not sharedQueue:
            condition.wait()
            print("empty queue")
        elementToReceive = sharedQueue.get(0)
        print("receivedData")
        [print(elementToReceive[i]) for i in list(elementToReceive.keys())]
        condition.release()
        time.sleep(random.random())


