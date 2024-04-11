import math
import datetime

start_time = datetime.datetime.now()
pi = math.pi
end_time = datetime.datetime.now()
print(pi)
print("程序运行时间{}".format(end_time-start_time))

start_time = datetime.datetime.now()
now_sum = 0.0
pre_sum = 0.0

for i in range(0, 1000):
    now_sum += math.factorial(4*i)*(1103+26390*i)/(math.factorial(i)**4*396**(4*i))
    delta = ((1/pre_sum) if pre_sum != 0 else math.inf) - 1/now_sum
    pre_sum = now_sum
    if delta < 1e-15 * 9801 / (2 * math.sqrt(2)):
        print("程序运行次数{}".format(i+1))
        break

ans = 1/(2*math.sqrt(2)/9801*now_sum)
end_time = datetime.datetime.now()
print("{:.16f}".format(ans))
print("程序运行时间{}".format(end_time-start_time))

