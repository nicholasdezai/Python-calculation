def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(isleap(2001))
