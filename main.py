from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width= 800, height = 600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down, "s")

score = ScoreBoard()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.r_move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()