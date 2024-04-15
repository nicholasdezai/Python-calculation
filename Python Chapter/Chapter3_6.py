num = eval(input("Enter a number(less than 1000): "))
# 对num因式分解
if num >= 1000:
    print("The number is too large.")
else:
    print("The prime factors are:")
    factor = 2
    while num != 1:
        if num % factor == 0:
            num = num / factor
            print(factor)
        else:
            factor += 1
