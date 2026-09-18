class RigidBody:
    def __init__(self, position, velocity, mass, material):
        self.position = position
        self.velocity = velocity       
        self.mass = mass
        self.material = material
        self.force = Vector3(0, 0, 0)
    
    def apply_force(self, force):
        # Add a force to the body's accumulated net force for this simulation step.
        self.force += force
        
    def clear_forces(self):
        self.force = Vector3(0, 0, 0)
        
    def __repr__(self):
        return (
        f"RigidBody("
        f"position={self.position}, "
        f"velocity={self.velocity}, "
        f"mass={self.mass}, "
        f"material={self.material}, "
        f"force={self.force})"
    )
    
    def copy(self):
        return RigidBody(
        position=self.position.copy(),
        velocity=self.velocity.copy(),
        mass=self.mass,
        material=self.material
    )
        
# RigidBody
#
# ├── Data
# │   ├── position      # Current position in world space.
# │   ├── velocity      # Current linear velocity.
# │   ├── mass          # Body mass (kg).
# │   ├── material      # Physical material.
# │   └── force         # Accumulated net force.
# │
# ├── Constructor
# │   └── __init__()    # Initialize the rigid body.
# │
# ├── Force Management
# │   ├── apply_force()     # Add an external force.
# │   └── clear_forces()    # Reset accumulated forces.
# │
# └── Utility
#     ├── __repr__()    # Readable string.
#     └── copy()        # Return an independent copy.

