import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()


screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()


screen.onkey(player.move_up, "Up")
car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.car_move()

    if player.ycor() >= 280:
        player.next_level()
        scoreboard.level += 1
        scoreboard.update_level()
        car_manager.increase_speed()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()




