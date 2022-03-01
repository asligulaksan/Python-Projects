from turtle import Turtle
ALIGN="center"
FONT=("Courier",80,"normal")

# STEP 8. Keep Score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def increase_r(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def increase_l(self):
        self.l_score += 1
        self.clear()
        self.update_score()
