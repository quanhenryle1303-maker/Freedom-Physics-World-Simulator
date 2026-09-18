class Material:
    def __init__(self, name, density):
        self.name = name
        self.density = density
    
    def __repr__(self):
        return f"Material(name={self.name}, density={self.density})"

# Material
#
# ├── Data
# │   ├── name          # Material name.
# │   └── density       # Density (kg/m³).
# │
# ├── Constructor
# │   └── __init__()    # Initialize a material.
# │
# └── Utility
#     └── __repr__()    # Readable string.