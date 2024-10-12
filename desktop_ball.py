import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.radius = 20
        self.id = canvas.create_oval(10, 10, 10 + 2*self.radius, 10 + 2*self.radius, fill=color)
        self.canvas.move(self.id, 245, 100)
        
        self.x = random.randrange(7, 13)
        self.y = random.randrange(7, 13)
        
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        
    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
    
    def resize(self, delta):
        self.radius = max(10, min(500, self.radius + delta)) #you can change the max size and min size
        pos = self.canvas.coords(self.id)
        x, y = (pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2
        self.canvas.coords(self.id, x - self.radius, y - self.radius, x + self.radius, y + self.radius)

root = tk.Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"] #add more colors if you want to
ball = Ball(canvas, random.choice(colors))

def update_ball():
    ball.canvas_width = root.winfo_width()
    ball.canvas_height = root.winfo_height()
    ball.move()
    root.after(random.randint(5, 20), update_ball)

def on_mousewheel(event):
    if event.delta > 0:
        ball.resize(5)
    else:
        ball.resize(-5)

root.bind("<MouseWheel>", on_mousewheel)

root.update()
update_ball()
root.mainloop()

# xxx from mapledev!