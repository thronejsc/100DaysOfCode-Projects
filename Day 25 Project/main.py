import turtle as t

import pandas
import pandas as p

FONT = ("Arial", 11, "normal")
screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
t.shape(image)

states = p.read_csv("50_states.csv")
states_correct = 0
total_states = len(states["state"])
states_list = states["state"].to_list()
correct_guess = []


while len(correct_guess) < 50:
    screen.tracer(1)
    answer_state = screen.textinput(title=f"{states_correct}/{total_states} States Correct", prompt="What's another state?").title()

    if answer_state == "Exit":
        forgot_states = []
        for state in states_list:
            if state not in correct_guess:
                forgot_states.append(state)
        new_df = pandas.DataFrame(forgot_states)
        new_df.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        state = states[states.state == answer_state]
        states_correct += 1
        correct_guess.append(answer_state)
        new_turtle = t.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(state.x[state.index[0]], state.y[state.index[0]])
        new_turtle.write(answer_state, align="center", font=FONT)



