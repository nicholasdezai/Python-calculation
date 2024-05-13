class Node:
    '''节点结构'''
    def __init__(self, data, nextNode=None):
        # 设置当前节点的值和指向下一个节点的指针
        self.data = data
        self.next = nextNode

    def insertAfter(self, node):
        # 在当前节点后面插入新节点
        node.next = self.next
        self.next = node

    def deleteAfter(self):
        # 删除当前节点后面的节点
        if self.next == None:
            return
        p = self.next
        self.next = p.next
        p.next = None
        del p
        
# 头节点
head = Node(0)
p = head
for i in range(1, 10):
    # 依次生成10个数字，并创建相应的节点
    # 把节点连接到链表的尾部
    n = Node(i)
    p.insertAfter(n)
    p = n

p = head
# 遍历链表节点，在值为3的节点后面插入值为3.5的新节点
while True:
    if p.data == 3:
        p.insertAfter(Node(3.5))
        break
    else:
        p = p.next
        
p = head
# 删除节点7后面的节点
while True:
    if p.data == 7:
        p.deleteAfter()
        break
    p = p.next
    if p.next == None:
        break

p = head
# 遍历链表并输出每个节点的值
while True:
    print(p.data)
    if p.next == None:
        break
    p = p.next
