import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, s_width, s_height):
        super().__init__()
        self.all_cars = []
        self.create_car(s_height, s_width)
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, s_height, s_width):
        should_create = random.randint(1, 6)
        if should_create == 6:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setx(s_width / 2)
            new_car.sety(random.randint(-s_height / 2 + 50, s_height / 2 - 50))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
