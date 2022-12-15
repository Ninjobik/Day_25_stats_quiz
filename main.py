from turtle import Turtle, Screen
import turtle
import pandas
import state

screen = Screen()
screen.setup(735, 500)
screen.title("USA States quuz by Ninjobik")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_guesses = []
missing_states = []
data = pandas.read_csv("50_states.csv")


def generate_log_csv():
    all_states = data.state.to_list()
    for each in all_states:
        if each not in correct_guesses:
            missing_states.append(each)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("missing_states.csv")


while len(correct_guesses) < 50:
    user_guess = screen.textinput(f"Guess the state {len(correct_guesses)}/50", "Write name of a state")
    if user_guess != '' and user_guess.title() not in correct_guesses:
        df = data[data.state == user_guess.title()]
        if user_guess.title() == "Exit":
            generate_log_csv()
            break
        if df.empty:
            print(user_guess.title())
        else:
            state.State(user_guess.title(), int(df.x), int(df.y))
            correct_guesses.append(df.state.item())
            print(correct_guesses)


# screen.exitonclick()
