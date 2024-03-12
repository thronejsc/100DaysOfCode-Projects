from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
    
    def left(self):
        if self.xcor() >= -360:
            new_x = self.xcor() - 30
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())
            
    
    def right(self):
        if self.xcor() <= 360:
            new_x = self.xcor() + 30
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())


