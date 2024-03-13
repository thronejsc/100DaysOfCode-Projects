from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_LINE = [-303, 200]
NUMBER_OF_ROWS = 4


class BrickManager:
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        

    def spawn_lines(self, number_of_bricks):
        
        for row in range(NUMBER_OF_ROWS):                            
            for i in range(number_of_bricks):
                new_brick = Turtle("square")
                new_brick.penup()
                new_brick.shapesize(stretch_wid=1, stretch_len=2.5)
                new_brick.color(choice(COLORS))
                new_brick.goto(START_LINE)
                self.all_bricks.append(new_brick)
                START_LINE[0] += 50
            START_LINE[0] = -303
            START_LINE[1] -= 20

        
    
        

    

