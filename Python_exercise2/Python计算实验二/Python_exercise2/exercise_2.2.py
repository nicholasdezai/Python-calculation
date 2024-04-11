# from swampy.TurtleWorld import *
#
# def koch_curve(t, length, level):
#     if level == 0:
#         fd(t, length)
#     else:
#         koch_curve(t, length / 3, level - 1)
#         lt(t, 30)
#         koch_curve(t, length / 3, level - 1)
#         rt(t, 90)
#         koch_curve(t, length / 3, level - 1)
#         lt(t, 60)
#         koch_curve(t, length / 3, level - 1)
#
#         koch_curve(t, length / 3, level - 1)
#         lt(t, 30)
#         koch_curve(t, length / 3, level - 1)
#         rt(t, 90)
#         koch_curve(t, length / 3, level - 1)
#         lt(t, 60)
#         koch_curve(t, length / 3, level - 1)
#
#
# world = TurtleWorld()
# bob = Turtle()
# bob.delay = 0.00  # 设置绘制延迟
#
# koch_curve(bob, 300, 3)
#
# wait_for_user()

# -*- coding: utf-8 -*-
#
# import numpy as np
# import matplotlib.pyplot as plot
#
# x0=0 #初始值z0的x0
# y0=0 #初始值z0的y0
# zoom=1.0 #放大倍率
# N=100 #最大迭代次数
# R=2 #迭代半径
# a=4.0 #绘制图的横轴大小
# b=3.0 #绘制图的纵轴大小
# step=0.005 #绘制点的步长
#
# def iterate(c,N,R):
#     z=c
#     for i in range(N):
#         if abs(z)>R:
#             return i
#         z = z*z+c
#     return N
#
# x=np.arange(-a/(2.0*zoom)+x0,a/(2.0*zoom)+x0,step)
# y=np.arange(b/(2.0*zoom)+y0,-b/(2.0*zoom)+y0,-step)
# cx,cy=np.meshgrid(x, y)
# c = cx + cy*1j
# ufunc=np.frompyfunc(iterate,3,1)
# Z=ufunc(c,N,R).astype(float)
# plot.imshow(Z,extent=(-a/2.0,a/2.0,-b/2,b/2.0))
# cb = plot.colorbar(orientation='vertical',shrink=1)
# cb.set_label('iteration counts')
# plot.show()


# -*- coding: utf-8 -*-

import matplotlib.pyplot as plot
import numpy as np

p = 0.45  # 初始值c的实部
q = -0.1428  # 初始值c的虚部
N = 800  # 最大迭代次数
M = 100  # 迭代区域的界值
a = 3.0  # 绘制图的横轴大小
b = 3.0  # 绘制图的纵轴大小
step = 0.005  # 绘制点的步长


def iterate(z, N, M):
    z = z * z + c
    for i in range(N):
        if abs(z) > M:
            return i
        z = z * z + c
    return N


c = p + q * 1j
i = np.arange(-a / 2.0, a / 2.0, step)
j = np.arange(b / 2.0, -b / 2.0, -step)
I, J = np.meshgrid(i, j)
ufunc = np.frompyfunc(iterate, 3, 1)
Z = ufunc(I + 1j * J, N, M).astype(float)
plot.imshow(Z, extent=(-a / 2.0, a / 2.0, -b / 2, b / 2.0))
cb = plot.colorbar(orientation='vertical', shrink=1)
cb.set_label('iteration counts')
plot.show()
