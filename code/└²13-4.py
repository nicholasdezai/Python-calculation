import time
import threading

class MyThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.name = threadName

    def run(self):             #线程运行的核心代码
        time.sleep(1)
        print('In run:', self.name)
        
    def output(self):          #在线程类中定义普通方法
        print('In output:', self.name)

t = MyThread('test')
t.start()                   #启动线程
t.output()                  #调用普通方法
time.sleep(2)
print('OK')
