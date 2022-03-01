from turtle import Turtle, Screen
import random

# Creating the screen
screen = Screen()
screen.setup(500,400)
# Adding title and user chooses the turtle
user_bet = screen.textinput(title="make your bet",prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False


colors = ["red","orange","yellow","green","blue","purple"]

turtles=[]
x = -230
y = +180

# Creating the turtles
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x,y)
    y -= 50
    turtles.append(new_turtle)

print(turtles)
if user_bet:
    is_race_on = True

#
while is_race_on:
    for turtle in turtles:
        # Checking the finishline
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        # Moving turtle
        random_distance= random.randint(0,10)
        turtle.forward(random_distance)















screen.exitonclick()

