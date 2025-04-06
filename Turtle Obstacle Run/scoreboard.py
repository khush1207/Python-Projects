from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 270)
        self.write(f"LEVEl: {self.level_num}",align="center", font=("Calibri", 15, "normal"))

    def increase_score(self):
        self.level_num += 1
        self.clear()
        self.write(f"LEVEl: {self.level_num}", align="center", font=("Calibri", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Calibri", 15, "normal"))
