import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        """
        30% chance to generate a new car
        :return:
        """
        if random.randint(1, 10) < 3:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setpos(300, random.randint(-240, 260))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def check(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
