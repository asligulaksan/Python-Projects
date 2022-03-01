from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.speed = STARTING_MOVE_DISTANCE

    # creating the cars
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)

    # moving the cars
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    # increasing the speed when level is passed
    def increase_speed(self):
        self.speed += MOVE_INCREMENT




