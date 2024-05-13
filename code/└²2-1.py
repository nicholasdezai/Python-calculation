import random
import time

def randomNumbers1(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    n = 0
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            n += 1
            if n == number:
                break
    return data

def randomNumbers2(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            if len(data) == number:
                break
    return data

def randomNumbers3(number, start, end):
    '''使用集合来生成number个介于start和end之间的不重复随机数'''
    data = set()
    while True:
        data.add(random.randint(start, end))
        if len(data) == number:
            break
    return data

def randomNumbers4(number, start, end):
    '''使用集合来生成number个介于start和end之间的不重复随机数'''
    data = set()
    n = 0
    while True:
        rnd = random.randint(start, end)
        if rnd not in data:
            data.add(rnd)
            n += 1
            if n == number:
                break
    return data

# 数字范围
begin, end = 1, 10000000
# 要获取的不重复数字个数
num = 20000
# 重复测试次数
rep = 10
print(f'{num=},{begin=},{end=}')
for ran in (randomNumbers4,randomNumbers3,randomNumbers2,randomNumbers1):
    start = time.time()
    for i in range(rep):
        ran(num, begin, end)
    print(ran.__name__, time.time()-start)
