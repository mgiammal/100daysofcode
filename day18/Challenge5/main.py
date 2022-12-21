import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


for _ in range(0, 360, 5):
    t.color(random_color())
    t.circle(radius=100)
    t.seth(_)

screen.exitonclick()
