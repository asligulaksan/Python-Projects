from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING = (-270,270)
ALIGN="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    # updating the level
    def update_level(self):
        self.goto(-270,270)
        self.write(f"Level: {self.level}", font=FONT)

    # increasing the level
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    # if turtle collide with a car, game overs
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

