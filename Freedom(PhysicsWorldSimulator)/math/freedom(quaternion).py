
import math
import importlib

freedom_module = importlib.import_module("freedom(vector3)")
Vector3 = freedom_module.Vector3


class Quaternion:
    # Constructor
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    # Properties
    def magnitude(self):
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def magnitude_squared(self):
        return self.w**2 + self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        L = self.magnitude()
        if L == 0:
            raise ValueError("Cannot normalize a zero quaternion")

        self.w /= L
        self.x /= L
        self.y /= L
        self.z /= L

    def normalized(self):
        L = self.magnitude()
        if L == 0:
            raise ValueError("Cannot normalize a zero quaternion")

        return Quaternion(
            self.w / L,
            self.x / L,
            self.y / L,
            self.z / L
        )

    # Public Methods
    def creation(self):
        return Quaternion(self.w, self.x, self.y, self.z)

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        mag_squared = self.magnitude_squared()

        if mag_squared == 0:
            raise ValueError("Zero quaternion has no inverse")

        conjugate = self.conjugate()

        return Quaternion(
            conjugate.w / mag_squared,
            conjugate.x / mag_squared,
            conjugate.y / mag_squared,
            conjugate.z / mag_squared
        )

    def to_axis_angle(self):
        mag = self.magnitude()

        if mag == 0:
            raise ValueError("Zero quaternion has no rotation")

        w = self.w / mag
        x = self.x / mag
        y = self.y / mag
        z = self.z / mag

        if w < 0:
            w, x, y, z = -w, -x, -y, -z

        w = max(-1.0, min(1.0, w))
        theta = 2 * math.acos(w)

        sin_half = math.sqrt(x*x + y*y + z*z)

        if sin_half < 1e-10:
            return Vector3(1, 0, 0), 0.0

        axis = Vector3(
            x / sin_half,
            y / sin_half,
            z / sin_half
        )

        return axis, theta

    # Static Methods
    @staticmethod
    def identity():
        return Quaternion(1, 0, 0, 0)

    @staticmethod
    def from_axis_angle(axis, theta):
        if axis.magnitude_squared() == 0:
            raise ValueError("Rotation axis cannot be zero")

        axis = axis.normalized()

        half_angle = theta / 2
        s = math.sin(half_angle)

        return Quaternion(
            math.cos(half_angle),
            axis.x * s,
            axis.y * s,
            axis.z * s
        )

    @staticmethod
    def dot(a, b):
        return (
            a.w * b.w +
            a.x * b.x +
            a.y * b.y +
            a.z * b.z
        )

    # Operators
    def __repr__(self):
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Quaternion(
            self.w + other.w,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Quaternion(
            self.w - other.w,
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, other):
        result_w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
        result_x = self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y
        result_y = self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x
        result_z = self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w

        return Quaternion(result_w, result_x, result_y, result_z)
