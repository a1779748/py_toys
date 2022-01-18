from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.color('black')
        self.movey = 0
        self.goto(STARTING_POSITION)

    def move(self):
        self.movey += MOVE_DISTANCE
        self.goto(0, self.movey)

    def reset_position(self):
        self.movey = -280
        self.goto(STARTING_POSITION)
