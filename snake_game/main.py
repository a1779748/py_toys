from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
# turn off the tracer, stop refreshing the screen
screen.tracer(0)


# Create snake on Screen
snake = Snake()
# Create Food on Screen
food = Food()
# Create ScoreBoard
scoreboard = Scoreboard()

# listing user's keyboard behaviour, change snake's move direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# let snake move
game_is_on = True
while game_is_on:
    # refreshing the screen every 1sec
    screen.update()
    time.sleep(0.1)
    # move snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with \ tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# keep the screen display
screen.exitonclick()
