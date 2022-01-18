from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create a 600 * 800 screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
# screen.screensize(canvwidth=800, canvheight=600)
screen.title('Pong Game')

# stop refresh screen
screen.tracer(0)

# create paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create a ball (width = 20, height = 20, x_pos = 0, y_pos = 0
ball = Ball()

# create a scoreboard
scoreboard = Scoreboard()

# listen the keyboard
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    # refresh screen
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # detect the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
