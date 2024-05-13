import threading
from time import sleep
from random import randint

#自定义生产者线程类
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self,name=threadname)
        
    def run(self):
        global x
        while True:
            sleep(1)
            con.acquire()                         #获取锁
            if len(x) == 5:                       #假设共享列表中最多能容纳5个元素
                print('Producer is waiting.....') #如果共享列表已满，生产者等待
                con.wait()
            else:
                r = randint(1, 1000)
                print('Produced:', r)             #产生新元素，添加至共享列表
                x.append(r)
                con.notify()                      #唤醒等待条件的线程
                
            con.release()                         #释放锁

#自定义消费者线程类
class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
        
    def run(self):
        global x
        while True:
            sleep(3)
            #获取锁
            con.acquire()
            if not x:
                #等待
                print('Consumer is waiting.....')
                con.wait()
            else:
                print('Consumed:', x.pop(0))
                con.notify()
                
            con.release()

#创建Condition对象以及生产者线程和消费者线程
con = threading.Condition()
x = []
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
c.start()
