import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

S_HEIGHT = 600
S_WIDTH = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.tracer(0)

player = Player()
cars = CarManager(S_WIDTH, S_HEIGHT)
score_board = Scoreboard(S_WIDTH, S_HEIGHT)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.create_car(S_WIDTH, S_HEIGHT)

    # Detect if turtle hit any car
    for car in cars.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            print("GAME OVER")

    if player.is_at_finish():
        cars.level_up()
        player.reset_position()
        score_board.increase_score()

screen.exitonclick()
