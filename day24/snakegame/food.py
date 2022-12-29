import random
from turtle import Turtle

OFFSET = 20


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.pu()
        self.speed("fastest")
        self.refresh(screen_width, screen_height)

    def refresh(self, screen_width, screen_height):
        rand_x = random.randint(-(screen_width / 2 - OFFSET), screen_width / 2 - OFFSET)
        rand_y = random.randint(-(screen_height / 2 - OFFSET), screen_height / 2 - OFFSET)
        self.goto(rand_x, rand_y)
