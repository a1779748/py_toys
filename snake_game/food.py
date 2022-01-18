import random
from turtle import Turtle


class Food(Turtle):
    """
    Food class is inheritance from Turtle class
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        create a new food randomly
        :return:
        """
        self.goto(random.randint(-280, 280), random.randint(-280, 280))