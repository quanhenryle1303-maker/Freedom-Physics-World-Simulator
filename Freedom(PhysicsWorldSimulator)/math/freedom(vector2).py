


class Vector2
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
  
        
    def __repr__(self):
        return f"Vector3({self.x}, {self.y},)"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar)
    
    def __floordiv__(self, scalar):
        return Vector3(self.x // scalar, self.y // scalar)

    def __mod__(self, scalar):
        return Vector3(self.x % scalar, self.y % scalar0
    
    def __pow__(self, scalar):
        return Vector3(self.x ** scalar, self.y ** scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        #Distance in Units
    
    def magnitude_squared(self) -> float:
        return self.x**2 + self.y**2 + self.z**2
        
    def normalize(self):
        L = self.magnitude()
        if L == 0:
            return 
        self.x /= L
        self.y /= L
        self.z /= L
        #Distance Divide Per Units
        #The vector Moves to Different Location
        
    def normalized(self):
        L = self.magnitude()
        if L == 0:
            return Vector2(0, 0)
        return Vector2(self.x / L, self.y / L)
    #ALso Divide Per Units
    #The Vector are Copied and The Copied One Moves to Different Location
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y-other.y)**)
    
    def distance_squared_to(self, other):
        return (self.x - other.x)**2 + (self.y-other.y)**2 
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        #IT just finding area, order matter
        #if vector self left to vector other = positive
        #if vector self right to vector other = negative