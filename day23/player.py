from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(90)
        self.shape("turtle")
        self.pu()
        self.color("black")
        self.reset_position()

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)
