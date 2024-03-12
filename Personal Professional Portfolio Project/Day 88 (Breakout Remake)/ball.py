from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.ball_speed = 0.1
        self.penup()
        self.setpos(x=-250, y=-40)
        self.x_move = 10
        self.y_move = -10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # self.ball_speed *= 0.9

    def back_to_center(self):
        self.setpos(0,0)
        self.ball_speed = 0.1
    
    def spawn(self):
        self.setpos(x=-250, y=-20)
        




