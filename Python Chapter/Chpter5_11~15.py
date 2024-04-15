def sum(l):
    total = 0
    for i in l:
        total += i
    return total


def sorted(arr, key=lambda x: x, reverse=False):
    # 快速排序的辅助函数，实现实际的排序逻辑
    def partition(low, high):
        # 选择最后一个元素作为主元
        pivot = key(arr[high])
        i = low - 1
        for j in range(low, high):
            # 根据reverse标志比较元素
            if (key(arr[j]) < pivot) != reverse:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_rec(low, high):
        # 递归进行快速排序
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    # 调用递归排序
    quick_sort_rec(0, len(arr) - 1)


def custom_sorted(iterable, key=lambda x: x, reverse=False):
    # 将可迭代对象转换为列表
    arr = list(iterable)
    # 使用快速排序对列表进行排序
    sorted(arr, key=key, reverse=reverse)
    # 返回排序后的列表
    return arr


# 使用示例
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(custom_sorted(data))  # 输出默认排序结果
print(custom_sorted(data, reverse=True))  # 输出逆序结果
print(custom_sorted(data, key=lambda x: -x))  # 通过key函数逆序排序


def map(function, iterable):
    """
    模拟内置的 map() 函数。应用函数到给定迭代器的每个元素。

    参数:
    function - 应用于每个元素的函数。
    iterable - 需要处理的迭代器。

    返回:
    一个迭代器，每次迭代返回应用函数后的元素。
    """
    for item in iterable:
        yield function(item)


# 使用示例
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)

# 打印结果来验证
print(list(result))  # 输出: [1, 4, 9, 16, 25]


def custom_filter(function, iterable):
    """
    模拟内置的 filter() 函数。过滤出满足条件的元素。

    参数:
    function - 应用于序列每个元素的函数，应返回布尔值。
    iterable - 需要被过滤的序列。

    返回:
    一个迭代器，包含所有使函数返回 True 的元素。
    """
    for item in iterable:
        if function(item):
            yield item


# 使用示例
def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_numbers = custom_filter(is_even, numbers)

# 打印结果来验证
print(list(filtered_numbers))  # 输出: [2, 4, 6, 8]


# 暴力
def filter(func, iterable):
    l = []
    for i in iterable:
        if func(i):
            l.append(i)
    return l
