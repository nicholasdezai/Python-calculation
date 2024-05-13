l = [i for i in range(100)]
# 反转
l.reverse()
print(l)

cnt_b = 0 # 记录比较次数
cnt_j = 0 # 记录交换次数
# qsort
def qsort(l):
    global cnt_b
    global cnt_j
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
        cnt_b += len(l) - 1
        cnt_j += len(l) - 1
        return qsort(less) + [pivot] + qsort(greater)

# 归并
def merge(left, right):
    global cnt_b
    global cnt_j
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        cnt_b += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            cnt_j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    middle = len(l) // 2
    left = l[:middle]
    right = l[middle:]
    return merge(merge_sort(left), merge_sort(right))

# 堆排序
def heapify(arr, n, i):
    global cnt_b
    global cnt_j
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    cnt_b += 1
    if l < n and arr[i] < arr[l]:
        largest = l
    cnt_b += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        cnt_j += 1
        heapify(arr, n, largest)

def heap_sort(arr):
    global cnt_b
    global cnt_j
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        cnt_j += 1
        heapify(arr, i, 0)
    return arr

qsort(l)

print(cnt_b)
print(cnt_j)