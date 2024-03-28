import random
import matplotlib.pyplot as plt
import pandas as pd

x = [random.random() for i in range(20)]

sorted_ = sorted(x[:10]) + sorted(x[10:], reverse=True)

print(sorted_)

plt.plot(sorted_)
plt.show()
