from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto((0, 0))
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        """
        move ball to x+xmove, y+ymove
        :return:
        """
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto((new_x, new_y))

    def bounce_y(self):
        """
        touch the up and down wall, so change the direction of ymove
        :return:
        """
        self.ymove *= -1

    def bounce_x(self):
        """
        paddle hit the ball, change the direction of xmove
        also increase the ball move speed
        :return:
        """
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        reset the ball's position to 0,0
        also, change the x direction of ball
        and reset ball's speed to 0.1
        :return:
        """
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
