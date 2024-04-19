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

    keep_playing = True
    while keep_playing:
        window.update()
        time.sleep(0.1)
        snake.move(20)

        if snake.head.distance(point) < 15:
            point.new_position()
            snake.extend_snake()
            score.add_points()

        if (snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or
                snake.head.ycor() < -340):
            keep_playing = False
            score.end_game()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                keep_playing = False
                score.end_game()
    window.exitonclick()
