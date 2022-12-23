from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def create_snake(self):
        position = 0
        for _ in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.pu()
            new_turtle.setx(position)
            self.segments.append(new_turtle)
            position -= MOVE_DIST

    def up(self):
        self.head.seth(UP) if DOWN != self.head.heading() else None

    def left(self):
        self.head.seth(LEFT) if RIGHT != self.head.heading() else None

    def down(self):
        self.head.seth(DOWN) if UP != self.head.heading() else None

    def right(self):
        self.head.seth(RIGHT) if LEFT != self.head.heading() else None
