import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data + other.data)
        elif isinstance(other, int) or isinstance(other, float):
            return Matrix(self.data + other)
        else:
            raise TypeError("Unsupported operand type for +: 'Matrix' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data - other.data)
        elif isinstance(other, int) or isinstance(other, float):
            return Matrix(self.data - other)
        else:
            raise TypeError("Unsupported operand type for +: 'Matrix' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(np.dot(self.data, other.data))
        else:
            raise TypeError("Unsupported operand type for *: 'Matrix' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(self.data * other)
        else:
            raise TypeError("Unsupported operand type for *: '{}' and 'Matrix'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return np.array_equal(self.data, other.data)
        else:
            return False
