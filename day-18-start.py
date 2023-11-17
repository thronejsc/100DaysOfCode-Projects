import turtle
from turtle import Turtle, Screen
#import as alias to make it short
#from turtle import as t
timmy = Turtle()

timmy.shape("turtle")
timmy.color("LightPink")


# Challenge 1, draw a square
def create_sqaure():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(10)
    timmy.right(90)

# Challenge 2, draw a dashed line
def dash_line():
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


from random import choice, randint


colors = ["MediumSlateBlue", "Plum", "HotPink", "Red", "OrangeRed", "Firebrick", "DarkOrange", "Orange", "Goldenrod"]
turtle.colormode(255)

# Create Random Color generator
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)

    return rgb
# Challenge 3, draw different shape
def draw_shapes(turns):
    degrees = 360 / turns
    for a in range(turns):
        timmy.forward(100)
        timmy.right(degrees)


# for i in range(3, 11):
#     timmy.color(choice(colors))
#     draw_shapes(i)


# Challenge 4, do a random walk
def random_walk():
    timmy.speed(8)
    random_color = choice(colors)
    timmy.dot(8, random_color)
    timmy.pensize(5)
    timmy.pencolor(random_color)
    degrees = [0, 90, 180, 270, 360]
    random_degrees = choice(degrees)
    timmy.forward(20)
    timmy.setheading(random_degrees)

# for i in range (100):
#     random_walk()

# Challenge 5, do challenge 4 but make a random color not based on a list

def random_color_walk():
    turtle.colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    timmy.color(rgb)
    timmy.speed(10)
    timmy.pensize(5)
    degrees = [0, 90, 180, 270, 360]
    random_degrees = choice(degrees)
    timmy.forward(20)
    timmy.setheading(random_degrees)

# for i in range (100):
#      random_color_walk()

def draw_spirograph(turns):
    degrees = 360 / turns
    timmy.speed("fastest")
    for i in range(0, turns):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(degrees)


draw_spirograph(60)


screen = Screen()

screen.exitonclick()



