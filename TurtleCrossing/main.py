import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating Player
player = Player()
# Creating obstacles
cars = CarManager()
# Creating scoreboard
level = Scoreboard()

# reading order from the keyboard
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # creating and moving the cars
    cars.create_car()
    cars.move_cars()


    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()

    # if player cross the cars, it goes to next level and back to its original position, updating the scoreboard and
    # increasing the speed of the cars
    if player.ycor() > 280:
        player.new_level()
        cars.increase_speed()
        cars.move_cars()
        level.increase_level()

screen.exitonclick()