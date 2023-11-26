from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.x_move = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_number = randint(1, 10)
        if random_number == 3 or random_number == 7:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            random_y = randint(-240, 270)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.x_move
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.x_move += MOVE_INCREMENT

