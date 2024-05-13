from random import choice, randint

def catchFox(n=5, maxTimes=10):
    #狐狸的初始位置，洞口从1到5编号
    currentPosition = randint(1, n)
    for i in range(maxTimes):
        x = int(input('请输入要打开的洞口编号(1-{})：'.format(n)))
        if x == currentPosition:
            print('成功！')
            break
        #到头，往回跳
        if currentPosition == 1:
            currentPosition += 1
        elif currentPosition == n:
            currentPosition -= 1
        else:
            #中间位置，随机左右跳
            currentPosition += choice((-1,1))
        #print('狐狸的当前位置：', currentPosition)
    else:
        print('失败。')

catchFox()
