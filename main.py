from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Yuen Yao's Snake Game")
screen.tracer(0)

# Create a snake
snake = Snake()
# Create a food
food = Food()

scoreboard = Scoreboard()

# Move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # If head collide with any square of the tail, trigger game over
    # The first item in the list is the head, so the dist between head and head is ofc 0, and it'll collide at the beginning
    for square in snake.all_squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()