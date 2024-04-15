class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)
        else:
            raise ValueError("Cannot divide by zero")

# 测试向量的加法、减法、乘法和除法运算
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

# 加法
print("Vector Addition:")
print(v1 + v2)  # 输出: Vector3D(5, 7, 9)

# 减法
print("Vector Subtraction:")
print(v1 - v2)  # 输出: Vector3D(-3, -3, -3)

# 标量乘法
print("Scalar Multiplication:")
print(v1 * 2)   # 输出: Vector3D(2, 4, 6)

# 标量除法
print("Scalar Division:")
print(v2 / 2)   # 输出: Vector3D(2.0, 2.5, 3.0)


