from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks_manager import BrickManager
from score import Scoreboard
import time 

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BREAKOUT!")
screen.tracer(0)

screen.listen()

bricks = BrickManager()
bricks.spawn_lines(13)
score = Scoreboard()
player = Paddle((0, -260))
ball = Ball()

screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_running = True

while game_is_running:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    # If you have no life left
    if score.lives == 0:
        score.game_over()
        game_is_running = False   
    
    # Detect collision with left and right wall
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.bounce_x()
    
    # Detect collision with upper part of wall    
    if ball.ycor() >= 290:
        ball.bounce_y()
        
    # Detect collision with paddle
    if (ball.distance(player) < 50 and ball.ycor() <= -250):
        ball.bounce_y()
    
    # Detect collision with bricks
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 28:
            brick.hideturtle()
            brick.goto(x=1000, y=1000)
            bricks.all_bricks.remove(brick)
            ball.bounce_y()
            score.add_point()
    
    # If all bricks are gone, end the game
    if not bricks.all_bricks:
        score.game_finished()
        game_is_running = False
    
    if score.lives == 0:
        score.game_over()
        game_is_running = False        
        
    # If ball goes outside 
    if ball.ycor() <= -320:
        score.deduct_life()
        ball.spawn()

screen.exitonclick()
