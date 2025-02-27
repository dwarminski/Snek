from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
