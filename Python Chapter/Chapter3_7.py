x = [i for i in range(1, 101) if i % 2 == 1]
print(sum(x))

sum = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum += i

print(sum)

odd_sum = 0

# 循环遍历1到100的奇数，步长为2
for num in range(1, 101, 2):
    odd_sum += num

print("1到100的奇数和为:", odd_sum)
