import string
import turtle as t
import pandas


def get_state_locations():
    return pandas.read_csv("50_states.csv")


screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

state_list = get_state_locations()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = string.capwords(screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                                    prompt="What's another state's name?"))
    answer_row = state_list[state_list.state == answer_state]

    if answer_state == "Exit":
        new_data = pandas.DataFrame([state for state in state_list.state if state not in guessed_states])
        new_data.to_csv("states_to_learn.csv")
        break
    if not answer_row.empty:
        guessed_states.append(answer_state)
        new_state = t.Turtle()
        new_state.pu()
        new_state.hideturtle()
        new_state.setpos(float(answer_row.x), float(answer_row.y))
        new_state.write(f"{answer_state}", align="center", font=("Courier", 10, "normal"))

screen.exitonclick()
