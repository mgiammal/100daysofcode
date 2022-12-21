import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
# need loop to draw shape based on num sides
colours = ["medium blue",
           "chartreuse",
           "gold",
           "crimson",
           "medium purple",
           "black",
           "saddle brown"]
for num_sides in range(3, 11):
    tim.color(random.choice(colours))
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
