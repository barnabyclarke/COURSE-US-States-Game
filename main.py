import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
guessed_states = []

screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)


def create_named_state(name, coordinates):
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(coordinates)
    new_state.write(f"{name}", align="center", font=("Courier", 8, "normal"))


def win_message():
    message = turtle.Turtle()
    message.hideturtle()
    message.color("red")
    message.write("Congratulations, you got all 50 States!", align="center", font=("Courier", 20, "normal"))


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"Guess the State {len(guessed_states)}/50", "State name:").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_info = states[states.state == answer_state]
        coord = (int(state_info.x), int(state_info.y))
        create_named_state(answer_state, coord)

if len(guessed_states) == 50:
    win_message()
else:
    missed_states = [state for state in states_list if state not in guessed_states]
    csv_data = pandas.DataFrame(missed_states)
    csv_data.to_csv("states_to_learn.csv")

screen.exitonclick()
