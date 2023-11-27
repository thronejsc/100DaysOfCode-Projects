from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

# open data.txt file to read the highscore
with open("data.txt") as file:
    contents = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(contents)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}" , False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            # overwrite the new highscore to the file
            with open("data.txt", mode="w") as newfile:
                newfile.write(str(self.score))
        self.score = 0
        self.update_score()




    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)

