l = [2]

for i in range(3, 1000):
    flag = True;
    for j in l:
        if i % j == 0:
            flag = False
            break
    if flag:
        l.append(i)
print(l)

import math
aList = [p for p in range(2, 1000) if 0 not in [p%d for d in range(2, int(math.sqrt(p))+1)]]
