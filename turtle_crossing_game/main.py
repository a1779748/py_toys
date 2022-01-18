import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # listen the keyboard
    screen.listen()
    screen.onkey(player.move, 'Up')
    car.generate_car()
    car.move()

    # collision with wall
    if player.ycor() > 280:
        player.reset_position()
        car.level_up()
        scoreboard.level_up()

    # collision with car
    if car.check(player):
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()