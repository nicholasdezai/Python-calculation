import math

pi = math.pi
print(pi)

now_sum = 0.0
pre_sum = 0.0


for i in range(0, 1000):
    now_sum += math.factorial(4*i)*(1103+26390*i)/(math.factorial(i)**4*396**(4*i))
    delta = 1/now_sum-(1/pre_sum) if pre_sum != 0 else 1
    pre_sum = now_sum
    if delta < 1e-15 * 9801 / (2 * math.sqrt(2)):
        break
ans = 1/(2*math.sqrt(2)/9801*now_sum)
print("{:.16f}".format(ans))

# print 1，Python流程控制;编写循环控制代码用下面公式融近圆周率(精确到小数点后15位)，并且和math-pi的值做比较，直到两者的差值小于1e-15为止。

