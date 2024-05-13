class SparseMatrix:
    '''使用字典表示和处理二维稀疏矩阵
    字典的键表示位置，值表示系数矩阵中该位置的值'''
    
    def __init__(self, lstMatrix=None):
        '''把二维列表转换为稀疏矩阵，或创建空矩阵'''
        self.__data = {}
        if lstMatrix is None:
            self.__size = (0, 0)
            return
        if len(set((len(row) for row in lstMatrix))) != 1:
            raise Exception('所有行必须长度一样')
        # 使用字典保存原始矩阵中非0元素的位置和值
        for rIndex, row in enumerate(lstMatrix):
            for cIndex, value in enumerate(row):
                value = float(value)
                if value != 0:
                    self.__data[(rIndex,cIndex)] = value
        # 矩阵尺寸
        self.__size = (len(lstMatrix), len(lstMatrix[0]))

    def toMatrix(self):
        '''转换为矩阵'''
        # 创建全0矩阵
        matrix = []
        for _ in range(self.__size[0]):
            matrix.append([0]*self.__size[1])
        # 修改非0元素
        for position, value in self.__data.items():
            r, c = position
            matrix[r][c] = value
        return '['+'\n '.join(map(str, matrix))+']'

    def __add_sub__(self, anotherSparseMatrix, op):
        '''两个矩阵的加法与减法运算通用代码'''
        if self.__size != anotherSparseMatrix.__size:
            raise Exception('尺寸不一致')
        result = SparseMatrix()
        result.__size = self.__size
        positions = tuple(self.__data.keys())+\
                    tuple(anotherSparseMatrix.__data.keys())
        for pos in positions:
            result.__data[pos] = eval(str(self.__data.get(pos, 0))+op+
                                      str(anotherSparseMatrix.__data.get(pos, 0)))
        return result

    def __add__(self, anotherSparseMatrix):
        '''两个矩阵相加'''
        return self.__add_sub__(anotherSparseMatrix, '+')
    
    def __sub__(self, anotherSparseMatrix):
        '''两个矩阵相减'''
        return self.__add_sub__(anotherSparseMatrix, '-')

    def __mul_div_truediv_pow(self, n, op):
        '''矩阵与标量乘法、整除、真除运算通用代码'''
        result = SparseMatrix()
        result.__size = self.__size
        for position, value in self.__data.items():
            result.__data[position] = eval(str(value)+op+str(n))
        return result

    def __mul_matrix(self, anotherMatrix):
        '''两个矩阵相乘'''
        result = SparseMatrix()
        result.__size = (self.__size[0], anotherMatrix.__size[1])
        for r in range(self.__size[0]):
            # 获取self矩阵中第r行，列表
            row = [0] * self.__size[1]
            for pos, value in self.__data.items():
                if pos[0] == r:
                    row[pos[1]] = value
            for c in range(anotherMatrix.__size[1]):
                # 获取anotherMatrix矩阵中第c列，列表
                col = [0] * anotherMatrix.__size[0]
                for pos, value in anotherMatrix.__data.items():
                    if pos[1] == c:
                        col[pos[0]] = value
                # 计算两个列表的内积，作为矩阵相乘结果中的一个元素
                dot = sum(map(lambda x,y: x*y, row, col))
                result.__data[(r,c)] = dot
        return result
    
    def __mul__(self, n):
        '''乘法，根据参数的不同，调用不同的运算'''
        if isinstance(n, (int, float)):
            return self.__mul_div_truediv_pow(n, '*')
        elif isinstance(n, SparseMatrix) and self.__size[1]==n.__size[0]:
            return self.__mul_matrix(n)
        else:
            raise Exception('数据类型不正确，或尺寸不合适')

    def __floordiv__(self, n):
        '''矩阵与数字整除'''
        assert isinstance(n, int), '除数必须为整数'
        return self.__mul_div_truediv_pow(n, '//')

    def __truediv__(self, n):
        '''真除'''
        return self.__mul_div_truediv_pow(n, '/')

    def __pow__(self, n):
        '''矩阵与数字的幂运算'''
        return self.__mul_div_truediv_pow(n, '**')

    def __str__(self):
        return 'SparseMatrix size:'+str(self.__size)+\
               ' NonZero elements:'+str(len(self.__data))

    __repr__ = __str__
