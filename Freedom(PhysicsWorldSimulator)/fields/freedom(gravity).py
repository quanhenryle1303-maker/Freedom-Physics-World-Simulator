
import importlib
import importlib.util
import sys
import os

file_path = r"C:\Users\quanh\Downloads\FreedomPython\Freedom(PhysicsWorldSimulator)\math\freedom(vector3).py"
spec = importlib.util.spec_from_file_location("freedom_module", file_path)
freedom_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(freedom_module)
Vector3 = freedom_module.Vector3

class Gravity:
    #Data
    def __init__(self, gravity=Vector3(0, -9.81, 0)):
        self.gravity = gravity
    
    def __bool__(self):
        return self.gravity
    
    #Core
    def sample(self, position):
        return self.gravity
    
    #Utility
    def magnitude(self):
        return (self.gravity).magnitude()
    
    def direction(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return Vector3(
            self.gravity.x / mag,
            self.gravity.y / mag,
            self.gravity.z / mag
        )
    def set_gravity(self, gravity):
        self.gravity = gravity
    
    
        