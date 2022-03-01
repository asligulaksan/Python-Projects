import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# STEP.1 : Create Snake Body
snake = Snake()

# STEP 4. Detect Collision with food
food = Food()

#STEP 5. Creating Scoreboard and Keep Score
score = ScoreBoard()

# STEP.3 : Control the Snake
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

# STEP.2 : Move the Snake
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

    #STEP 4. Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

    # STEP 7. Detect colling with tail
        snake.extend()

        #STEP 5. Creating Scoreboard and Keep Score
        score.increase()

    # STEP 6. Detect colling with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        snake.reset_snake()
        score.reset()


    # STEP 7. Detect colling with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            score.reset()

screen.exitonclick()