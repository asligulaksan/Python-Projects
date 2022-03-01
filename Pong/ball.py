from turtle import Turtle
# STEP 4. Create the ball and make it move
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # STEP 5. Detect collision with ball and bounce
    def bounce_y(self):
        self.y_move *= -1
    # STEP 6. Detect collision with paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # STEP 7. Detect collision with paddle
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()