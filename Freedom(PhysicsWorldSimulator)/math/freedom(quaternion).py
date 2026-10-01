import math
import importlib
freedom_module = importlib.import_module("freedom(vector3)")
Vector3 = freedom_module.Vector3


class Quaternion:
    def __init__(self, w:float, x:float, y:float, z:float):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"
    
    def identity():
        return [1, 0, 0, 0]

        