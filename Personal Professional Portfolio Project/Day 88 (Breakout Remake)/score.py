from turtle import Turtle
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update()

    def update(self):
        self.clear()
        self.goto(-345, -290)
        self.write(f"SCORE: {self.score}", align="center", font=FONT)
        self.goto(340, -290)
        self.write(f"LIVES: {self.lives}", align="center", font=FONT)      
        
    def add_point(self):
        self.score += 40
        self.update()
    
    def deduct_life(self):
        self.lives -= 1
        self.update()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.YOU LOSE.", False, align="center", font=GAME_OVER_FONT)
        
    def game_finished(self):
        self.goto(0, 0)
        self.write("CONGRATULATIONS!\nYOU WIN!", False, align="center", font=GAME_OVER_FONT)

