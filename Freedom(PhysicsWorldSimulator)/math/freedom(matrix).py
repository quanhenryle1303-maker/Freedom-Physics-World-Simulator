import math
import importlib
freedom_module = importlib.import_module("freedom(vector3)")
Vector3 = freedom_module.Vector3


class Matrix4:
    def __init__(self, element=None):
        self.element = element
    
    def creation(elements):
        return Matrix4(elements)
    
    @staticmethod
    def identity():
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    
    def __mul__(self, other):
         # Make sure we are multiplying two Matrix4 objects
        if not isinstance(other, Matrix4):
            raise TypeError("Can only multiply Matrix4 by Matrix4")

        # Create an empty 4x4 matrix for the result
        result = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        # Go through every row of the first matrix
        for row in range(4):

            # Go through every column of the second matrix
            for column in range(4):

                # Multiply the row of the first matrix
                # by the column of the second matrix
                for k in range(4):
                    result[row][column] += (
                        self.elements[row][k] *
                        other.elements[k][column]
                    )
                    

        # Return the newly created Matrix4
        return Matrix4(result)
    
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
        
        # Perspective division.
        # Only divide when w is not zero.
        if result_w != 0:
            result_x /= result_w
            result_y /= result_w
            result_z /= result_w
            
        return Vector3(result_x, result_y, result_z)
    
    def transpose(self):
        # Swap rows and columns
        result = [
            [self.elements[j][i] for j in range(4)]
            for i in range(4)
        ]

        return Matrix4(result)
    
    def _determinant_3x3(self, m):
        #M=[[​a, b, c], [d, e, f], [g, h, i]]​
        #det(M)=a(ei−fh)−b(di−fg)+c(dh−eg)
        
        return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        )
    
    def determinant(self):
        det = 0
        
        #Go Over the Matrix Column
        for columns in range(4):
            #Creates a 3*3 Minor List (Now EMpty Will be Added later)
            minor = []
            #Ranging the columns to 3*3
            for i in range(1, 4):
                #Rows that will be Makes THrough code and finally form a 3*3
                row = []
                #Go over the Rows
                for j in range(4):
                    if j != columns: #If the Rows not Belong to the Column
                        #Yes it's accurate to include it in Matrix 3*3 
                        row.append(self.elements[i][j])
                #After Formulate all 3*3 then that will go to Minot
                minor.append(row)

            sign = 1 if columns % 2 == 0 else -1 #In Determinant it iwll always like + - + - even column index = +, odd column index = -
            
            det += (sign * self.elements[0][columns] * self._determinant_3x3(minor)) #An Equation for 4*4 Determinant
        
        return det #After Done All The Matrix
    
    def inverse(self):
        det = self.determinant()

        # A matrix with determinant 0 cannot be inverted
        if det == 0:
            raise ValueError("Matrix is not invertible")

        cofactors = [
            [0 for _ in range(4)]
            for _ in range(4)
        ]

        for row in range(4):
            for column in range(4):

                # Build the 3x3 minor
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

                # Cofactor sign
                sign = 1 if (row + column) % 2 == 0 else -1

                cofactors[row][column] = (
                    sign * self._determinant_3x3(minor)
                )

        # Transpose the cofactor matrix
        adjugate = [
            [cofactors[j][i] for j in range(4)]
            for i in range(4)
        ]

        # Divide every element by the determinant
        result = [
            [adjugate[i][j] / det for j in range(4)]
            for i in range(4)
        ]

        return Matrix4(result)
        
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
        
            # Rotation around X axis
        rx = Matrix4([
            [1, 0, 0, 0],
            [0, cx, -sx, 0],
            [0, sx, cx, 0],
            [0, 0, 0, 1]
        ])

        # Rotation around Y axis
        ry = Matrix4([
            [cy, 0, sy, 0],
            [0, 1, 0, 0],
            [-sy, 0, cy, 0],
            [0, 0, 0, 1]
        ])

        # Rotation around Z axis
        rz = Matrix4([
            [cz, -sz, 0, 0],
            [sz, cz, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # Combine the three rotations
        return rz * ry * rx