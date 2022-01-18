from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        clear the scoreboard and update the score
        :return:
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Courier', 80, 'normal'))

    def l_point(self):
        """
        increase the left paddle's score
        :return:
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        increase the left paddle's score
        :return:
        """
        self.r_score += 1
        self.update_scoreboard()