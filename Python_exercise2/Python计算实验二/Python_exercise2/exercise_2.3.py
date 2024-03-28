import random
import pandas as pd
import matplotlib.pyplot as plt

# M = eval(input("请输入班级数:"))
# N = eval(input("请输入班级人数:"))

for j in range(1000):
    Q = 0
    for k in range(1, 1000):
        l = [random.randint(1, 365) for i in range(j)]
        d = dict()
        flag = False
        for i in l:
            if i in d:
                flag = True
            else:
                d[i] = 1
        if flag:
            Q += 1
    print(Q / 1000)
