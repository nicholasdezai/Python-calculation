import threading
from time import sleep
from queue import Queue

class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global myqueue
        sleep(1)
        myqueue.put(self.getName())
        print(self.getName(), 'put', self.getName(), 'to queue.')

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global myqueue
        sleep(1)
        print(self.getName(), 'get', myqueue.get(), 'from queue.')

myqueue = Queue()
plist = []
clist = []

for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

for i in plist:
    i.start()
    #i.join()           # 这里的join()本身已经起到了同步的作用
for i in clist:
    i.start()
    #i.join()
