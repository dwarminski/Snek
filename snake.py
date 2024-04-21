from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.another_segment(position)

    def another_segment(self, position):
        body_part = Turtle(shape="square")
        body_part.color("white")
        body_part.pu()
        body_part.goto(position)
        self.segments.append(body_part)

    def extend_snake(self):
        self.another_segment(self.segments[-1].position())

    def move(self, distance):
        for segm_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segm_num - 1].xcor()
            new_y = self.segments[segm_num - 1].ycor()
            self.segments[segm_num].goto(new_x, new_y)
        self.head.forward(distance)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for segm in self.segments:
            segm.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
