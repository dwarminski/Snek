from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=320)
        self.display_points()

    def display_points(self):
        self.write(arg=f"Score:{self.points}", move=False, align="center", font=('Arial', 15, 'normal'))

    def add_points(self):
        self.clear()
        self.points += 1
        self.display_points()
