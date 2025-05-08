from turtle import Turtle,Screen
import random
screen = Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(x=0,y=0)
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.move_x *= -1
        self.ball_speed *= 0.9

    def switch(self):
        self.ball_speed = 0.1
        self.goto(0,0)
        self.bounce_x()


