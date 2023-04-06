from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Declarations
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def main():
    game_alive = True
    while game_alive:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()
            # game_alive = False
            # scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                # game_alive = False
                # scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()

