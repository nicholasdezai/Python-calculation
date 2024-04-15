import random

l = [random.randint(1, 100) for i in range(50)]
print(l)
# 删除奇数
l = [i for i in l if i % 2 == 0]
print(l)
