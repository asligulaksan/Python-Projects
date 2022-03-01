from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # STEP 4. Detect Collision with food
    def refresh(self):
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x=x_cor, y=y_cor)

