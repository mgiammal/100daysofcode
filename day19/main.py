from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win? Pick your color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
turtle_list = []

y_start = -100
for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.pu()
    new_turtle.goto(x=-225, y=y_start)
    turtle_list.append(new_turtle)
    y_start += 30

game_on = False
if user_input:
    game_on = True

while game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_input.lower() == winning_color:
                print(f"You've won! The winning turtle was: {winning_color}")
            else:
                print(f"You've lost. You guessed {user_input.lower()} but the winning turtle was: {winning_color}")
            game_on = False
        dist = random.randint(0, 10)
        turtle.forward(dist)


screen.exitonclick()
