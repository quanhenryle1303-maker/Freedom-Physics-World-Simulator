import tkinter as tk

class PhysicsSim:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Physics Simulation")
        
        # Setup Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        # Physics Variables
        self.x, self.y = 300, 50      # Initial position
        self.radius = 20
        self.vx = 2                    # Horizontal velocity
        self.vy = 0                    # Vertical velocity
        self.gravity = 0.5             # Gravity acceleration
        self.elasticity = 0.75         # Bounciness (energy retained)
        
        # Draw Ball
        self.ball = self.canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill="crimson"
        )
        
        # Start Simulation Loop
        self.update_physics()

    def update_physics(self):
        # 1. Apply Gravity to Vertical Velocity
        self.vy += self.gravity
        
        # 2. Update Positions
        self.x += self.vx
        self.y += self.vy
        
        # 3. Check Floor Collision (Height = 400)
        if self.y + self.radius >= 400:
            self.y = 400 - self.radius  # Snap to floor
            self.vy = -self.vy * self.elasticity  # Reverse and dampen velocity
            
        # 4. Check Wall Collisions (Width = 600)
        if self.x + self.radius >= 600 or self.x - self.radius <= 0:
            self.vx = -self.vx * self.elasticity
            
        # 5. Move the Canvas Shape
        # canvas.coords requires coordinates for bounding box: (x1, y1, x2, y2)
        self.canvas.coords(
            self.ball, 
            self.x - self.radius, self.y - self.radius, 
            self.x + self.radius, self.y + self.radius
        )
        
        # 6. Loop again in 16ms (~60 Frames Per Second)
        self.root.after(16, self.update_physics)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    sim = PhysicsSim(root)
    root.mainloop()
