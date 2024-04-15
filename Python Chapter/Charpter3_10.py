import random

def simulate_monty_hall(num_trials, switch_door):
    win_count = 0
    for _ in range(num_trials):
        # 随机放置汽车和山羊
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # 参赛者随机选择一扇门
        contestant_choice = random.randint(0, 2)

        # 主持人打开一扇有山羊的门，但不是参赛者选择的门
        remaining_doors = [i for i in range(3) if i != contestant_choice]
        for door in remaining_doors:
            if doors[door] == 'goat':
                show_goat = door
                break
        remaining_doors.remove(show_goat)

        # 参赛者决定是否改变选择
        if switch_door:
            contestant_choice = remaining_doors[0]

        # 检查是否赢得汽车
        if doors[contestant_choice] == 'car':
            win_count += 1

    return win_count / num_trials

# 模拟次数
num_trials = 10000

# 不改变选择的中奖概率
win_rate_stay = simulate_monty_hall(num_trials, switch_door=False)
# 改变选择的中奖概率
win_rate_switch = simulate_monty_hall(num_trials, switch_door=True)

print(f"不改变选择时赢得汽车的概率为：{win_rate_stay:.2f}")
print(f"改变选择时赢得汽车的概率为：{win_rate_switch:.2f}")
