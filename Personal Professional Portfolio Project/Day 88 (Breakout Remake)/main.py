from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks_manager import BrickManager
import time 

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BREAKOUT!")
screen.tracer(0)

screen.listen()

brick = BrickManager()
brick.spawn_line1(12)
player = Paddle((0, -260))
ball = Ball()

screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_running = True

while game_is_running:
    time.sleep(ball.ball_speed)
    screen.update()
    # ball.move()
    
    
    
    # # Detect collision with left and right wall
    # if ball.xcor() >= 390 or ball.xcor() <= -390:
    #     ball.bounce_x()
    
    # # Detect collision with upper part of wall    
    # if ball.ycor() >= 290:
    #     ball.bounce_y()
        
    # # Detect collision with paddle
    # if (ball.distance(player) < 50 and ball.ycor() < -240):
    #     ball.bounce_y()
        
    # # If ball goes outside 
    # if ball.ycor() <= -320:
    #     ball.spawn()

screen.exitonclick()
