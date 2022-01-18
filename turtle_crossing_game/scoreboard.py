from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update()

    def game_over(self):
        self.color('black')
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", align="center", font=FONT)

    def update(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()
