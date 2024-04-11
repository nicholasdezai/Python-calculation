import random
from collections import OrderedDict


def Ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return Ack(m - 1, 1)
    else:
        return Ack(m - 1, Ack(m, n - 1))


print(Ack(3, 4))


def remove_repeat(l):
    return list(OrderedDict.fromkeys(l))


l = [random.randint(0, 100) for i in range(1000)]
print(l)
l = remove_repeat(l)
print(l)
