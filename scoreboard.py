from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as file:
            self.highscore = file.read()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=320)
        self.display_points()

    def display_points(self):
        self.clear()
        self.write(arg=f"Score:{self.points} High Score: {self.highscore}", move=False, align="center",
                   font=('Arial', 15, 'normal'))

    def add_points(self):
        self.points += 1
        self.display_points()

    def reset(self):
        if self.points > int(self.highscore):
            self.highscore = self.points
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.points = 0
        self.display_points()

    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over", move=False, align="center", font=('Arial', 15, 'normal'))
