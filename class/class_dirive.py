class BaseClass:
    def show(self):
        print('BaseClass.show()')


class A(BaseClass):
    def show(self):
        print('A.show()')
        super().show()
        print("exit A.show()")


class B(BaseClass):
    def show(self):
        print('B.show()')
        super().show()
        print("exit B.show()")


class C(BaseClass):
    def show(self):
        print('C.show()')
        super().show()
        print("exit C.show()")


class D(A, B, C):
    def show(self):
        print('D.show()')
        super().show()
        print("exit D.show()")


d = D()
d.show()
