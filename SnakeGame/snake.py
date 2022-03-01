from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0

class Snake:
    # STEP.1 : Create Snake Body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # STEP.2 : Move the Snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # STEP 7. Detect colling with tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # STEP.3 : Control the Snake
# If current is pointed up, then it cannot go down
    def left(self):
        if self.head.heading() != RIGHT_DIRECTION: #when direction is not pointed on the opposite direction
            self.head.setheading(LEFT_DIRECTION)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION: #when direction is not pointed on the opposite direction
            self.head.setheading(RIGHT_DIRECTION)

    def up(self):
        if self.head.heading() != DOWN_DIRECTION: #when direction is not pointed on the opposite direction
            self.head.setheading(UP_DIRECTION)

    def down(self):
        if self.head.heading() != UP_DIRECTION: #when direction is not pointed on the opposite direction
            self.head.setheading(DOWN_DIRECTION)

    # More functions

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]









