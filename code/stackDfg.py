'''
Author: 董付国
微信公众号：Python小屋，关注人数52000人，分享文章近900篇
email: dongfuguo2005@126.com
Date: 2014-11-10, Updated on 2019-10-28
'''
class Stack:
    def __init__(self, size=10):
        '''创建栈对象并进行初始化，默认栈大小为10'''
        # 使用列表存放栈的元素
        self.__content = []
        # 初始栈大小
        self.__size = size
        # 栈中元素个数初始化为0
        self.__current = 0
        
    def empty(self):
        '''清空栈'''
        self.__content = []
        self.__current = 0
        
    def isEmpty(self):
        '''测试栈是否为空'''
        return not self.__content

    def setSize(self, size):
        '''调整栈的大小，可以增大或缩小栈空间'''
        # 如果缩小空间时指定的新大小，小于已有元素个数
        # 则删除指定大小之后的已有元素
        if size < self.__current:
            for i in range(size, self.__current)[::-1]:
                del self.__content[i]
            self.__current = size
        self.__size = size
    
    def isFull(self):
        '''测试栈是否已满'''
        return self.__current == self.__size
        
    def push(self, v):
        '''将新元素入栈'''
        # 模拟入栈，需要先测试栈是否已满
        if self.__current < self.__size:
            self.__content.append(v)
            # 栈中元素个数加1
            self.__current = self.__current+1
        else:
            print('Stack Full!')

    def __str__(self):
        return str(self.__content)

    __repr__ = __str__
            
    def pop(self):
        '''将栈顶元素出栈'''
        # 模拟出栈，需要先测试栈是否为空
        if self.__content:
            # 栈中元素个数减1
            self.__current = self.__current-1
            return self.__content.pop()
        else:
            print('Stack is empty!')
            
    def show(self):
        '''显示当前栈对象中的元素'''
        print(self.__content)

    def showRemainderSpace(self):
        '''显示栈对象剩余空间大小'''
        print('Stack can still PUSH ', self.__size-self.__current, ' elements.')
