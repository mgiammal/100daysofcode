from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

S_WIDTH = 800
S_HEIGHT = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Game")

position = 0
game_on = True

right_paddle = Paddle(side="right")
left_paddle = Paddle(side="left")
ball = Ball()
score_board = ScoreBoard(S_HEIGHT)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

x_boundary = S_WIDTH/2 - 20
y_boundary = S_HEIGHT/2 - 20

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > x_boundary:
        score_board.increase_score_l()
        ball.reset_position()

    if ball.xcor() < -x_boundary:
        score_board.increase_score_r()
        ball.reset_position()

    if ball.ycor() > y_boundary or ball.ycor() < -y_boundary:
        # Ball method to change direction
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and
                                                                    ball.xcor() < -320):
        ball.bounce_x()

screen.exitonclick()
