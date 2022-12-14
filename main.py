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

while len(correct_guesses) < 50:
    user_guess = screen.textinput(f"Guess the state {len(correct_guesses)}/50", "Write name of a state")
    data = pandas.read_csv("50_states.csv")
    if user_guess != '' and user_guess.title() not in correct_guesses:
        df = data[data.state == user_guess.title()]
        if df.empty:
            print(user_guess.title())
        else:
            state.State(user_guess.title(), int(df.x), int(df.y))
            correct_guesses.append(df.state.item())
            print(correct_guesses)


screen.exitonclick()
