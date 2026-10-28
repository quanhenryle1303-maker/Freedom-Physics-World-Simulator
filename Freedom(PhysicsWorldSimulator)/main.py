import tkinter as tk
import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class Matrix4x4:
    def __init__(self):
        # Initialize as an Identity Matrix
        self.m = [[0.0]*4 for _ in range(4)]
        for i in range(4):
            self.m[i][i] = 1.0

    @staticmethod
    def multiply_vector(matrix, vec):
        """Multiplies a Vector3 by a 4x4 Matrix (Homogeneous Coordinates)"""
        x = vec.x * matrix.m[0][0] + vec.y * matrix.m[1][0] + vec.z * matrix.m[2][0] + matrix.m[3][0]
        y = vec.x * matrix.m[0][1] + vec.y * matrix.m[1][1] + vec.z * matrix.m[2][1] + matrix.m[3][1]
        z = vec.x * matrix.m[0][2] + vec.y * matrix.m[1][2] + vec.z * matrix.m[2][2] + matrix.m[3][2]
        w = vec.x * matrix.m[0][3] + vec.y * matrix.m[1][3] + vec.z * matrix.m[2][3] + matrix.m[3][3]
        
        if w != 0.0:
            return Vector3(x / w, y / w, z / w)
        return Vector3(x, y, z)

    @staticmethod
    def create_rotation_y(angle_deg):
        """Matrix for turning left/right (Yaw)"""
        rad = math.radians(angle_deg)
        mat = Matrix4x4()
        mat.m[0][0] = math.cos(rad)
        mat.m[0][2] = -math.sin(rad)
        mat.m[2][0] = math.sin(rad)
        mat.m[2][2] = math.cos(rad)
        return mat

    @staticmethod
    def create_rotation_x(angle_deg):
        """Matrix for looking up/down (Pitch)"""
        rad = math.radians(angle_deg)
        mat = Matrix4x4()
        mat.m[1][1] = math.cos(rad)
        mat.m[1][2] = math.sin(rad)
        mat.m[2][1] = -math.sin(rad)
        mat.m[2][2] = math.cos(rad)
        return mat

class Matrix3DWorld:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix & Vector Powered 3D Engine")
        
        self.canvas = tk.Canvas(root, width=600, height=600, bg="#0a0a14")
        self.canvas.pack()
        
        # Camera Vectors
        self.camera_pos = Vector3(0, 0, -300)
        self.yaw = 0.0    # Left / Right angle
        self.pitch = 0.0  # Up / Down angle
        
        # World Object: A 3D Cube built out of our Vector3 class
        self.cube_vertices = [
            Vector3(-50, -50, 50), Vector3(50, -50, 50), Vector3(50, 50, 50), Vector3(-50, 50, 50),
            Vector3(-50, -50, 150), Vector3(50, -50, 150), Vector3(50, 50, 150), Vector3(-50, 50, 150)
        ]
        
        self.edges = [
            (0,1), (1,2), (2,3), (3,0),
            (4,5), (5,6), (6,7), (7,4),
            (0,4), (1,5), (2,6), (3,7)
        ]
        
        # Key bindings
        self.root.bind("<w>", lambda e: self.move_camera(0, 15))
        self.root.bind("<s>", lambda e: self.move_camera(0, -15))
        self.root.bind("<a>", lambda e: self.move_camera(-15, 0))
        self.root.bind("<d>", lambda e: self.move_camera(15, 0))
        
        # Arrow keys to manipulate the rotation matrices
        self.root.bind("<Left>", lambda e: self.rotate_camera(-5, 0))
        self.root.bind("<Right>", lambda e: self.rotate_camera(5, 0))
        self.root.bind("<Up>", lambda e: self.rotate_camera(0, 5))
        self.root.bind("<Down>", lambda e: self.rotate_camera(0, -5))
        
        self.render()

    def move_camera(self, side, forward):
        rad = math.radians(self.yaw)
        self.camera_pos.x += forward * math.sin(rad) + side * math.cos(rad)
        self.camera_pos.z += forward * math.cos(rad) - side * math.sin(rad)
        self.render()

    def rotate_camera(self, yaw_change, pitch_change):
        self.yaw += yaw_change
        # Limit pitch so the camera doesn't flip upside down
        self.pitch = max(-80, min(80, self.pitch + pitch_change))
        self.render()

    def pipeline(self, vertex):
        """Passes a vector through the transformation matrix pipeline"""
        # 1. Translate relative to camera position
        rel_vec = Vector3(vertex.x - self.camera_pos.x, vertex.y - self.camera_pos.y, vertex.z - self.camera_pos.z)
        
        # 2. Apply Rotation Matrices
        mat_yaw = Matrix4x4.create_rotation_y(-self.yaw)
        mat_pitch = Matrix4x4.create_rotation_x(-self.pitch)
        
        transformed = Matrix4x4.multiply_vector(mat_yaw, rel_vec)
        transformed = Matrix4x4.multiply_vector(mat_pitch, transformed)
        
        # Don't render if it's behind the lens
        if transformed.z <= 10:
            return None
            
        # 3. Project to 2D
        focal = 400
        sx = (transformed.x * focal) / transformed.z + 300
        sy = (-transformed.y * focal) / transformed.z + 300
        return (sx, sy)

    def render(self):
        self.canvas.delete("all")
        
        # UI Info
        self.canvas.create_text(300, 30, text=f"Yaw: {int(self.yaw)}° | Pitch: {int(self.pitch)}°", fill="white")
        
        projected = []
        for v in self.cube_vertices:
            projected.append(self.pipeline(v))
            
        for edge in self.edges:
            p1 = projected[edge[0]]
            p2 = projected[edge[1]]
            if p1 and p2:
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#00ffcc", width=2)

if __name__ == "__main__":
    window = tk.Tk()
    app = Matrix3DWorld(window)
    window.mainloop()
