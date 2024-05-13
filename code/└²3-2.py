numbers = []                              #  使用列表存放临时数据
while True:
    x = input('请输入一个成绩：')
    try:                                  # 异常处理结构
        x = float(x)
        if 0 <= x <= 100:
            numbers.append(x)
        else:
            print('不是合法成绩')
    except:
        print('不是合法成绩')
    while True:
        flag = input('继续输入吗？（yes/no）').lower()
        if flag not in ('yes', 'no'):     # 限定用户输入内容必须为yes或no
            print('只能输入yes或no')
        else:
            break
    if flag == 'no':
        break

print(round(sum(numbers)/len(numbers), 1))
