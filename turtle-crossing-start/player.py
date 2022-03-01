from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # moving the turtle
    def move(self):
        self.forward(10)

    # moving back to turtle its original position
    def new_level(self):
        self.goto(STARTING_POSITION)


