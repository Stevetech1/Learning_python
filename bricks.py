import turtle

class Brick(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, 100)
        self.destroyed = False

    def destroy(self):
        self.hideturtle()
        self.destroyed = True

    def is_destroyed(self):
        return self.destroyed

    def render(self):
        pass  # Render the brick on the screen
