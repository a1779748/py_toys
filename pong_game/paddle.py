from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # pong paddle (width = 20, height = 100, x_pos = 350, y_pos = 0)
        self.penup()
        self.shape('square')
        # turtl start with 20*20, following will stretch it to 20*5, 20*1
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(position)

    def go_up(self):
        """
        move paddle up
        :return:
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        move paddle down
        :return:
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)