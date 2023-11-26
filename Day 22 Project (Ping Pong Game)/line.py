from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setheading(270)
        self.pensize(5)
        self.goto(0, 300)
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
