from turtle import Screen
import time
from day20.snake import Snake
from food import Food
from scoreboard import ScoreBoard

S_WIDTH = 600
S_HEIGHT = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

position = 0
game_on = True

snake = Snake()
food = Food(screen_width=S_WIDTH, screen_height=S_HEIGHT)
score_board = ScoreBoard(screen_height=S_HEIGHT)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x_boundary = S_WIDTH/2 - 10
y_boundary = S_HEIGHT/2 - 10

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food and move food
    if snake.head.distance(food) < 15:
        food.refresh(S_WIDTH, S_HEIGHT)
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > x_boundary or snake.head.xcor() < -x_boundary  or snake.head.ycor() < -y_boundary or snake.\
            head.ycor() > y_boundary:
        game_on = False
        score_board.game_over()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score_board.game_over()


screen.exitonclick()
