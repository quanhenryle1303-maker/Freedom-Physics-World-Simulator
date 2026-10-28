
import math

class Vector3:
    # Constructor
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    # Properties
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def magnitude_squared(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        L = self.magnitude()
        if L == 0:
            return
        self.x /= L
        self.y /= L
        self.z /= L

    def normalized(self):
        L = self.magnitude()
        if L == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / L, self.y / L, self.z / L)

    # Public Methods
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 +
                         (self.y - other.y)**2 +
                         (self.z - other.z)**2)

    def distance_squared_to(self, other):
        return ((self.x - other.x)**2 +
                (self.y - other.y)**2 +
                (self.z - other.z)**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)

    def lerp(self, other, t0):
        t = max(0, min(1, t0))
        x = self.x + t * (other.x - self.x)
        y = self.y + t * (other.y - self.y)
        z = self.z + t * (other.z - self.z)
        return Vector3(x, y, z)

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def to_list(self):
        return [self.x, self.y, self.z]

    # Operators
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __floordiv__(self, scalar):
        return Vector3(self.x // scalar, self.y // scalar, self.z // scalar)

    def __mod__(self, scalar):
        return Vector3(self.x % scalar, self.y % scalar, self.z % scalar)

    def __pow__(self, scalar):
        return Vector3(self.x ** scalar, self.y ** scalar, self.z ** scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector3):
            return False
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
