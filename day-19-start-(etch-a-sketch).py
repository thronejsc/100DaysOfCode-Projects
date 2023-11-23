from turtle import Screen, Turtle

t = Turtle()
s = Screen()

# move forward
def move_forwards():
    t.forward(50)

# move backward
def move_backwards():
    t.backward(50)

# turn counterclockwise "a"
def turn_counter_clockwise():
    t.left(30)


# turn clockwise "d"
def turn_clockwise():
    t.right(30)


# clear screen, reset turtle position
def clear():
    t.clear()
    t.teleport(0, 0)
    t.setheading(0)


s.listen()
s.onkey(key='w', fun=move_forwards)
s.onkey(key='s', fun=move_backwards)
s.onkey(key='a', fun=turn_counter_clockwise)
s.onkey(key='d', fun=turn_clockwise)
s.onkey(key='c', fun=clear)

s.exitonclick()