# 1. make the snake
from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia's Snake Game Remake!!!")
screen.tracer(0)
snake = Snake()

# 5. create a score board
score = Scoreboard()

# 4. detect collision with food
food = Food()

# 3. control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. move the snake
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        score.update_score()
        # increase snake length
        snake.extend()

    # 6. detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or \
            snake.head.ycor() > 280 or snake.head.ycor() < -285:
        snake.head.hideturtle()
        #to hide removed parts of snake on screen
        while len(snake.segments) != 3:
            snake.segments[-1].hideturtle()
            snake.segments.remove(snake.segments[-1])
        snake.head.goto(0, 0)
        snake.head.showturtle()
        score.reset()

# 7. detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()


screen.exitonclick()
