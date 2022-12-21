###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

# Paint Hirst 10 by 10 dots #
# Dot size 20 #
# 50 paces between dots #
import turtle as t
import random

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tom = t.Turtle()
t.colormode(255)
tom.pu()
screen = t.Screen()
spacing = 50
tom.speed("fast")
tom.seth(225)
tom.forward(250)
tom.seth(0)
start_x = tom.position()[0]

horizontal_dots = 10
vertical_dots = 10

for i in range(vertical_dots):
    cur_y = tom.position()[1]
    for _ in range(horizontal_dots):
        cur_x = tom.position()[0]
        tom.dot(20, random.choice(colors))
        tom.setx(cur_x + spacing)
    tom.setposition(start_x, cur_y + 50)

screen.exitonclick()
