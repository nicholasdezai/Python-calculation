class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour % 24
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        seconds = self.time2int() + other.time2int()
        time_temp = Time()
        time_temp = time.int2time(seconds)
        return time_temp

    def time2int(self):
        # 异常处理时间是否合法
        if not self.isvalid():
            print('Invalid time')
            return

        return self.hour * 3600 + self.minute * 60 + self.second

    def int2time(self, seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        time.hour = time.hour % 24
        return time

    def printtime(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def isafter(self, other):
        return self.time2int() > other.time2int()

    def increment(self, seconds):
        seconds += self.time2int()
        return self.int2time(seconds)

    def isvalid(self):
        if self.hour < 0 or self.hour > 23:
            return False
        if self.minute < 0 or self.minute > 59:
            return False
        if self.second < 0 or self.second > 59:
            return False
        return True


time = Time(1, 2, 3)
print("time.__str__ =", time.__str__())
print("time.time2int =", time.time2int())
print("time+other =", time.__add__(Time(1, 0, 0)))
time.printtime()
print("time.isafter =", time.isafter(Time(23, 0, 0)))
print("time.increment =", time.increment(3600))
print("time.isvalid =", time.isvalid())
