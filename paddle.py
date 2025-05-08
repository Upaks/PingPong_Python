from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)


    def up(self):
        y = self.ycor()
        self.sety(y + 20)

    def down(self):
        y = self.ycor()
        self.sety(y - 20)
