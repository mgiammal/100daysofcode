import turtle
from turtle import Turtle

# Drawing A Dashed Line
# Draw 10 paces, move 10 paces, repeat 50 times

tom = Turtle()
tom.color("red")

for _ in range(50):
    tom.forward(10)
    tom.pu()
    tom.forward(10)
    tom.pd()
