from copy import deepcopy
import numpy as np
import scipy.signal as signal

x = np.arange(0, 6, 0.1)
y = np.sin(x)
z = deepcopy(y)                                     # 深复制，备份，修改z不会影响y
print('='*20, 'y:', y, sep='\n')
print('before adding noise. z-y:', z-y, sep='\n')
index = np.random.randint(0, len(x), 20)
noise = np.random.standard_normal(20) * 0.8         # 生成噪声数据
z[index] += noise                                   # 添加噪声
print('='*20, 'after adding noise. z-y:', z-y, sep='\n')
result = signal.medfilt(z, 3)                       # 中值滤波，邻域大小为3
print('='*20, 'after median filtering. z-y:', result-y, sep='\n')
