import turtle as t
import random

tim = t.Turtle()
tim.pen(pensize=10)
tim.speed("fast")

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

for _ in range(random.randint(0, 1000)):
    tim.color(random.choice(colours))
    tim.seth(random.randrange(0, 360, 90))
    tim.forward(35)
