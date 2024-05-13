class BaseClass(object):
    def show(self):
        print('BaseClass')

class SubClassA(BaseClass):
    def show(self):
        print('Enter SubClassA')
        super().show()
        print('Exit SubClassA')

class SubClassB(BaseClass):
    def show(self):
        print('Enter SubClassB')
        super().show()
        print('Exit SubClassB')

class SubClassC(BaseClass):
    def show(self):
        print('Enter SubClassC')
        super().show()
        print('Exit SubClassC')

class SubClassD(SubClassA, SubClassB, SubClassC):
    def show(self):
        print('Enter SubClassD')
        super().show()
        print('Exit SubClassD')

d = SubClassD()
d.show()
print(SubClassD.mro())
