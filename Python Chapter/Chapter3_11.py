def nim_sum(heaps):
    """计算尼姆和"""
    nimsum = 0
    for heap in heaps:
        nimsum ^= heap
    return nimsum


def perfect_move(heaps, nimsum):
    """找出完美的移动策略"""
    for i, heap in enumerate(heaps):
        target = nimsum ^ heap
        if target < heap:
            return (i, heap - target)
    return (0, 1)  # 没有必胜策略时随便移除一个


def player_move(heaps):
    """玩家移动"""
    while True:
        print("当前各堆的石头数量:", heaps)
        pile = int(input("选择要移除石头的堆（0开始编号）："))
        if 0 <= pile < len(heaps):
            remove = int(input("选择要移除的石头数量："))
            if 1 <= remove <= heaps[pile]:
                return (pile, remove)
        print("无效的移动，请重新输入！")


def main():
    # 初始化堆的数量
    heaps = [3, 4, 5]
    current_player = "玩家"  # 玩家先手

    while any(heaps):
        print(f"当前玩家: {current_player}")
        if current_player == "玩家":
            pile, remove = player_move(heaps)
        else:
            ns = nim_sum(heaps)
            pile, remove = perfect_move(heaps, ns)
            print(f"电脑从堆 {pile} 移除 {remove} 枚石头。")

        heaps[pile] -= remove
        if not any(heaps):
            print(f"{current_player} 赢了！")
            break
        current_player = "电脑" if current_player == "玩家" else "玩家"


if __name__ == "__main__":
    main()
