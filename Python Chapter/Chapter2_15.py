import random

d = {}

for i in range(1000):
    a = random.randint(0, 100)
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(d)
