"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""

class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

# 这段代码定义了一个名为Kangaroo的类，表示袋鼠。该类具有以下功能：
# __init__(self, contents=[])：初始化方法，用于创建Kangaroo对象并初始化其袋子中的内容。默认情况下，袋子是空的。
# __str__(self)：返回该Kangaroo对象及其袋子中内容的字符串表示形式，每行表示一个内容。
# put_in_pouch(self, item)：将新物品添加到袋子中。
# 接下来，创建了两个Kangaroo对象（kanga和roo），并将一些物品和另一个Kangaroo对象放入kanga的袋子里。最后，通过打印kanga对象来显示其袋子中的内容。
