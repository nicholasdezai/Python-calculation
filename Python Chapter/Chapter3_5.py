import random
l = [random.randint(1, 100) for i in range(20)]
print(l)
# 对偶数下标降序排列
l[::2] = sorted(l[::2], reverse=True)
print(l)
