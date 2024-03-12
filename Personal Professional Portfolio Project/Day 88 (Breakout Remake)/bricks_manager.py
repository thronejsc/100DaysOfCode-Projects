from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class BrickManager:
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        

    def spawn_line1(self, number):
        starting_x = -250
        starting_y = 200
        # random_number = randint(1, 10)
        # if random_number == 3 or random_number == 7:
        #     new_car = Turtle("square")
        #     new_car.penup()
        #     new_car.shapesize(stretch_wid=1, stretch_len=2)
        #     new_car.color(choice(COLORS))
        #     random_y = randint(-240, 270)
        #     new_car.goto(300, random_y)
        #     self.all_cars.append(new_car)
            
        for i in range(number):
            new_brick = Turtle("square")
            new_brick.penup()
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.color(choice(COLORS))
            new_brick.goto(starting_x, starting_y)
            self.all_bricks.append(new_brick)
            starting_x += 45
            

    

