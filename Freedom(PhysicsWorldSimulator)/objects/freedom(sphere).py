import math

class Sphere(RigidBody):
    def __init__(self, radius, position, velocity, mass, material):
        # Call the parent class (RigidBody) constructor. super()
        # This initializes all common physics properties:
        # position, velocity, mass, material, and force.
        super().__init__(position, velocity, mass, material)
        self.radius = radius
        
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)
    
    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def __repr__(self):
        return (
        f"Sphere("
        f"radius={self.radius}, "
        f"position={self.position}, "
        f"velocity={self.velocity}, "
        f"mass={self.mass}, "
        f"material={self.material}, "
        f"force={self.force})"
        )
        
    def copy(self):
        return Sphere(
        radius=self.radius,
        position=self.position.copy(),
        velocity=self.velocity.copy(),
        mass=self.mass,
        material=self.material
        )
    
    def vertices(self):
        hw = self.width / 2
        hh = self.height / 2
        hd = self.depth / 2

        return [
            Vector3(-hw, -hh, -hd),
            Vector3( hw, -hh, -hd),
            Vector3( hw,  hh, -hd),
            Vector3(-hw,  hh, -hd),
            Vector3(-hw, -hh,  hd),
            Vector3( hw, -hh,  hd),
            Vector3( hw,  hh,  hd),
            Vector3(-hw,  hh,  hd)
        ]
    
    
def edges(self):
    return [
        # First face (z = -hd)
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),

        # Opposite face (z = +hd)
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),

        # Connect the two faces
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    ]

        