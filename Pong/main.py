from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# STEP 1. Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# STEP 2. Create and move a paddle
# STEP 3. Create another paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# STEP 4. Create the ball and make it move
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # STEP 4. Create the ball and make it move
    ball.move()

    # STEP 5. Detect collision with ball and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # STEP 6. Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed()

    # STEP 7. Detect when the paddle misses
    # STEP 8. Keep Score
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()



screen.exitonclick()



# STEP 2. Create and move a paddle
# STEP 3. Create another paddle
# STEP 4. Create the ball and make it move
# STEP 5. Detect collision with ball and bounce
# STEP 6. Detect collision with paddle
# STEP 7. Detect when the paddle misses
# STEP 8. Keep Score