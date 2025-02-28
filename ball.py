
from turtle import Turtle,Screen
from random import random, randint,choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        # creating the ball w = 20, h = 20, x = 0 , y = 0

        self.shape("circle")#--
        self.color("white")#--
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    # moving ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

# think and understand
    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
