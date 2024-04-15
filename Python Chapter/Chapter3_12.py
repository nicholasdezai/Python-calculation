def nth_ugly_number(n):
    # 丑数数组，初始化第一个丑数
    ugly_numbers = [1]
    # 初始化三个指针，用于指向2, 3, 5的倍数
    i2 = i3 = i5 = 0

    # 当生成的丑数数量少于 n 时，继续生成
    while len(ugly_numbers) < n:
        # 分别计算三个指针指向的丑数与其对应质因子的乘积
        next2, next3, next5 = ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5
        # 选取这三个产品中的最小值作为下一个丑数
        next_ugly = min(next2, next3, next5)
        ugly_numbers.append(next_ugly)

        # 如果最小值是哪个指针的结果，就将那个指针向前移动
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1

    return ugly_numbers[-1]


# 查找第150个丑数
l = [nth_ugly_number(i) for i in range(1, 100) if nth_ugly_number(i)<100]
print(l)
