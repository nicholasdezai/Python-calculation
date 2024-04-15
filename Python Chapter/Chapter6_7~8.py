class CustomSet:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def size(self):
        return len(self.elements)

    def contains(self, element):
        return element in self.elements

# 测试自定义集合类
custom_set = CustomSet()
custom_set.add(1)
custom_set.add(2)
custom_set.add(3)

print("Set size:", custom_set.size())  # 输出: 3

custom_set.remove(2)
print("Set contains 2:", custom_set.contains(2))  # 输出: False

class Deque:
    def __init__(self):
        self.elements = []

    def append_left(self, element):
        self.elements.insert(0, element)

    def append_right(self, element):
        self.elements.append(element)

    def pop_left(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            return None

    def pop_right(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def size(self):
        return len(self.elements)

# 测试自定义双端队列类
deque = Deque()
deque.append_left(1)
deque.append_right(2)
deque.append_left(3)

print("Deque size:", deque.size())  # 输出: 3

print("Deque:", deque.elements)  # 输出: [3, 1, 2]

print("Pop left:", deque.pop_left())  # 输出: 3
print("Pop right:", deque.pop_right())  # 输出: 2

print("Deque after pops:", deque.elements)  # 输出: [1]