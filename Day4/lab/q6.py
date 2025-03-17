import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, vector):
        if isinstance(vector, Vector):
            return Vector(self.x + vector.x, self.y + vector.y)
        else:
            raise TypeError("Unsupported operand type for +: 'Vector' and '{}'".format(type(vector).__name__))

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            return Vector(self.x - vector.x, self.y - vector.y)
        else:
            raise TypeError("Unsupported operand type for -: 'Vector' and '{}'".format(type(vector).__name__))

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for *: 'Vector' and '{}'".format(type(scalar).__name__))

    def __eq__(self, vector):
        if isinstance(vector, Vector):
            return self.x == vector.x and self.y == vector.y
        else:
            return False

    def __len__(self):
        magnitude = math.sqrt(self.x**2 + self.y**2)
        return round(magnitude)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range. Valid indices are 0 and 1.")

v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 == Vector(2, 4))
print(len(v1))
print(v1[0])
print(v1[1])
