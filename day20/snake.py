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
        position = (0.0, 0.0)
        for _ in range(3):
            self.add_segment(position)
            position = (position[0] - MOVE_DIST, position[1])

    def up(self):
        self.head.seth(UP) if DOWN != self.head.heading() else None

    def left(self):
        self.head.seth(LEFT) if RIGHT != self.head.heading() else None

    def down(self):
        self.head.seth(DOWN) if UP != self.head.heading() else None

    def right(self):
        self.head.seth(RIGHT) if LEFT != self.head.heading() else None

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.pu()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
