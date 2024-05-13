import random

memo = {}


def quicksort_comparisons(arr):
    if len(arr) <= 1:
        return 0
    pivot = arr[random.randint(0, len(arr) - 1)]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]
    return len(arr) - 1 + quicksort_comparisons(less) + quicksort_comparisons(greater)


def generate_sequence_with_comparison(n, target_comparison):
    sequence = list(range(1, n + 1))
    current_comparison = quicksort_comparisons(sequence)

    # 检查是否存在已计算的解
    if current_comparison == target_comparison:
        return sequence

    if (tuple(sequence), current_comparison) in memo:
        return memo[(tuple(sequence), current_comparison)]

    while current_comparison != target_comparison:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        sequence[i], sequence[j] = sequence[j], sequence[i]

        new_comparison = quicksort_comparisons(sequence)
        print("Current sequence:", sequence, "Comparisons:", new_comparison)  # 打印当前序列和比较次数

        if abs(new_comparison - target_comparison) < abs(current_comparison - target_comparison):
            current_comparison = new_comparison
        else:
            sequence[i], sequence[j] = sequence[j], sequence[i]

    # 缓存结果
    memo[(tuple(sequence), current_comparison)] = sequence
    return sequence


target_comparison = 480
n = 100
sequence = generate_sequence_with_comparison(n, target_comparison)
print(sequence)
print("Comparisons:", quicksort_comparisons(sequence))
