from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def space():
    screen = Screen()
    screen.setup(width=700, height=700)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


if __name__ == '__main__':
    window = space()
    snake = Snake()
    point = Food()
    score = Scoreboard()

    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.left, "Left")
    window.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        window.update()
        time.sleep(0.1)
        snake.move(20)

        if snake.head.distance(point) < 15:
            point.new_position()
            score.add_points()

    window.exitonclick()
