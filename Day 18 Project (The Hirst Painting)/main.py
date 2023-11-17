import turtle as t
import colorgram
from turtle import Turtle, Screen
from random import randint, choice

# colors = colorgram.extract("hirst.jpg", 20)
#
# color_list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
#
#
# print(color_list)\

t.colormode(255)
color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (39, 249, 42)]

# Requirements
# 10 x 10
# dot size 20, space 50

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

def hirst_painting():
    height = 10
    width = 10
    tim.penup()
    tim.setposition(-225, -200)
    tim.pendown()
    while height != 0:
        tim.setheading(0)
        for i in range(width):
            random_color = choice(color_list)
            tim.dot(20, random_color)
            tim.penup()
            tim.forward(50)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        for i in range(width):
            tim.forward(50)
        height -= 1


hirst_painting()











screen = Screen()
screen.exitonclick()

