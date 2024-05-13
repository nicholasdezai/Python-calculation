# -*- coding:utf-8 -*-
# Filename: myQueue.py
# --------------------
# Function description:
# Queue of my own implementation
# --------------------
# Author: 董付国
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-11-13, Updated on 2021-8-28
# --------------------

import time

class myQueue:
    def __init__(self, size = 10):
        self.__content = []
        self.__size = size
        self.__current = 0

    def setSize(self, size):
        if size < self.__current:
            # 如果缩小队列，应删除后面的元素
            for i in range(size, self.__current)[::-1]:
                del self.__content[i]
            self.__current = size
        self.__size = size

    def put(self, v, timeout=999999):
        # 模拟入队，在列表尾部追加元素
        # 队列满，阻塞，超时放弃
        for i in range(timeout):            
            if self.__current < self.__size:
                self.__content.append(v)
                self.__current = self.__current+1
                break
            time.sleep(1)
        else:
            return '队列已满，超时放弃'

    def get(self, timeout=999999):
        # 模拟出队，从列表头部弹出元素
        # 队列为空，阻塞，超时放弃
        for i in range(timeout):            
            if self.__content:
                self.__current = self.__current-1
                return self.__content.pop(0)
            time.sleep(1)
        else:
            return '队列为空，超时放弃'

    def show(self):
        # 如果列表非空，输出列表
        if self.__content:
            print(self.__content)
        else:
            print('The queue is empty')
        
    def empty(self):
        self.__content = []
        self.__current = 0

    def isEmpty(self):
        return not self.__content

    def isFull(self):
        return self.__current == self.__size

if __name__ == '__main__':
    print('Please use me as a module.')
