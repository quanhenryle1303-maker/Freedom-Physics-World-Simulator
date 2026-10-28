
import math
import importlib

freedom_module = importlib.import_module("freedom(vector3)")
Vector3 = freedom_module.Vector3


class Matrix4:
    # Constructor
    def __init__(self, elements=None):
        self.elements = elements

    # Public Methods
    def multiply_vector(self, vector):
        x = vector.x
        y = vector.y
        z = vector.z
        w = 1

        result_x = (
            self.elements[0][0] * x +
            self.elements[0][1] * y +
            self.elements[0][2] * z +
            self.elements[0][3] * w
        )

        result_y = (
            self.elements[1][0] * x +
            self.elements[1][1] * y +
            self.elements[1][2] * z +
            self.elements[1][3] * w
        )

        result_z = (
            self.elements[2][0] * x +
            self.elements[2][1] * y +
            self.elements[2][2] * z +
            self.elements[2][3] * w
        )

        result_w = (
            self.elements[3][0] * x +
            self.elements[3][1] * y +
            self.elements[3][2] * z +
            self.elements[3][3] * w
        )

        if result_w != 0:
            result_x /= result_w
            result_y /= result_w
            result_z /= result_w

        return Vector3(result_x, result_y, result_z)

    def transpose(self):
        result = [
            [self.elements[j][i] for j in range(4)]
            for i in range(4)
        ]
        return Matrix4(result)

    def determinant(self):
        det = 0

        for column in range(4):
            minor = []

            for i in range(1, 4):
                row = []

                for j in range(4):
                    if j != column:
                        row.append(self.elements[i][j])

                minor.append(row)

            sign = 1 if column % 2 == 0 else -1
            det += sign * self.elements[0][column] * self._determinant_3x3(minor)

        return det

    def inverse(self):
        det = self.determinant()

        if det == 0:
            raise ValueError("Matrix is not invertible")

        cofactors = [[0 for _ in range(4)] for _ in range(4)]

        for row in range(4):
            for column in range(4):
                minor = []

                for i in range(4):
                    if i == row:
                        continue

                    minor_row = []

                    for j in range(4):
                        if j == column:
                            continue
                        minor_row.append(self.elements[i][j])

                    minor.append(minor_row)

                sign = 1 if (row + column) % 2 == 0 else -1
                cofactors[row][column] = sign * self._determinant_3x3(minor)

        adjugate = [
            [cofactors[j][i] for j in range(4)]
            for i in range(4)
        ]

        result = [
            [adjugate[i][j] / det for j in range(4)]
            for i in range(4)
        ]

        return Matrix4(result)

    # Static Methods
    @staticmethod
    def creation(elements):
        return Matrix4(elements)

    @staticmethod
    def identity():
        return Matrix4([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def translation(x, y, z):
        return Matrix4([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def scale(x, y, z):
        return Matrix4([
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def rotation(x, y, z):
        cx = math.cos(x)
        sx = math.sin(x)

        cy = math.cos(y)
        sy = math.sin(y)

        cz = math.cos(z)
        sz = math.sin(z)

        rx = Matrix4([
            [1, 0, 0, 0],
            [0, cx, -sx, 0],
            [0, sx, cx, 0],
            [0, 0, 0, 1]
        ])

        ry = Matrix4([
            [cy, 0, sy, 0],
            [0, 1, 0, 0],
            [-sy, 0, cy, 0],
            [0, 0, 0, 1]
        ])

        rz = Matrix4([
            [cz, -sz, 0, 0],
            [sz, cz, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        return rz * ry * rx

    # Operators
    def __mul__(self, other):
        if not isinstance(other, Matrix4):
            raise TypeError("Can only multiply Matrix4 by Matrix4")

        result = [[0 for _ in range(4)] for _ in range(4)]

        for row in range(4):
            for column in range(4):
                for k in range(4):
                    result[row][column] += (
                        self.elements[row][k] *
                        other.elements[k][column]
                    )

        return Matrix4(result)

    # Internal Helpers
    def _determinant_3x3(self, m):
        return (
            m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        )
