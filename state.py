from turtle import Turtle


class State(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.setposition(x, y)
        self.write(f"{state_name}", False, "center", ("Ariel", 10, "normal" ))
