import math

class Cube(RigidBody):
    def __init__(self, width, height, depth, position, velocity, mass, material):
        # Call the parent class (RigidBody) constructor. super()
        # This initializes all common physics properties:
        # position, velocity, mass, material, and force.
        super().__init__(position, velocity, mass, material)
        
        self.width = width
        self.height = height
        self.depth = depth
    
    def volume(self):
        return self.width * self.height * self.depth
    
    def surface_area(self):
        return 2 * (self.depth * self.width + 
                    self.width * self.height + 
                    self.depth * self.height)
    def __repr__(self):
        return (
            f"Cube("
            f"width={self.width}, "
            f"height={self.height}, "
            f"depth={self.depth}, "
            f"position={self.position}, "
            f"velocity={self.velocity}, "
            f"mass={self.mass}, "
            f"material={self.material}, "
            f"force={self.force})"
        )


    def copy(self):
        return Cube(
            width=self.width,
            height=self.height,
            depth=self.depth,
            position=self.position.copy(),
            velocity=self.velocity.copy(),
            mass=self.mass,
            material=self.material
        ) 
    

# Cube
#
# ├── Inherited from RigidBody
# │   ├── position        # Location in world space.
# │   ├── velocity        # Current linear velocity.
# │   ├── mass            # Mass of the body.
# │   ├── material        # Physical material properties.
# │   └── force           # Accumulated net force.
# │
# ├── Cube Data
# │   ├── width           # Length along the X axis.
# │   ├── height          # Length along the Y axis.
# │   └── depth           # Length along the Z axis.
# │
# ├── Constructor
# │   └── __init__()      # Initialize rigid body and cube dimensions.
# │
# ├── Geometry
# │   ├── volume()        # Calculate cube volume.
# │   └── surface_area()  # Calculate cube surface area.
# │
# └── Utility
#     ├── __repr__()      # Return readable debug information.
#     └── copy()          # Create an independent copy.