import importlib
import importlib.util
import sys
import os

file_path = r"C:\Users\quanh\Downloads\FreedomPython\Freedom(PhysicsWorldSimulator)\math\freedom(vector3).py"
spec = importlib.util.spec_from_file_location("freedom_module", file_path)
freedom_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(freedom_module)
Vector3 = freedom_module.Vector3

class Camera:
    def __init__(self, position=Vector3()):
        self.position = position
    
    def forward(self, target=Vector(3)):
        return (target - self.position).normalized() 
    
    def up(self):
        return self.position.y
    
    def right(self):
        return self.position.z