import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")


rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_names = ["tim", "tin", "tib", "tip", "tik", "tig", "tif"]
game_start = False

y = -100
turtles = []
for (colors, names) in zip(rainbow, turtle_names):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors)
    new_turtle.name = names
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 30


if bet:
    game_start = True

while game_start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_start = False
            winner_color = turtle.pencolor()
            if winner_color == bet:
                print(f"You win!. The {winner_color} turtle is the winner!")
            else:
                print(f"You lose!. The {winner_color} turtle is the winner!")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)


# tim = Turtle(shape="turtle")
# tim.penup()
# tin = Turtle(shape="turtle")
# tin.penup()
# tib = Turtle(shape="turtle")
# tib.penup()
# tip = Turtle(shape="turtle")
# tip.penup()
# tik = Turtle(shape="turtle")
# tik.penup()
# tig = Turtle(shape="turtle")
# tig.penup()
# tif = Turtle(shape="turtle")
# tif.penup()

# tim.goto(x=-230, y=-100)
# tin.goto(x=-230, y=-70)
# tib.goto(x=-230, y=-40)
# tip.goto(x=-230, y=-10)
# tik.goto(x=-230, y=20)
# tig.goto(x=-230, y=50)
# tif.goto(x=-230, y=80)




screen.exitonclick()