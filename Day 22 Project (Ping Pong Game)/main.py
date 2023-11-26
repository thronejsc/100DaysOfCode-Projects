from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard
screen = Screen()


screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

screen.listen()
paddle_one = Paddle((350, 0))
paddle_two = Paddle((-360, 0))
scoreboard = Scoreboard()
line = Line()
ball = Ball()

screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")

screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")


game_is_running = True

while game_is_running:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(paddle_one) < 40 and ball.xcor() > 320) or (ball.distance(paddle_two) < 60 and ball.xcor() < -340):
        ball.bounce_x()

    # Detect if ball goes outside
    if ball.xcor() > 400:  # right side
        ball.back_to_center()
        scoreboard.left_point()
        ball.bounce_x()

    elif ball.xcor() < -420:  # left side
        ball.back_to_center()
        scoreboard.right_point()
        ball.bounce_x()



screen.exitonclick()