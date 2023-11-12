def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
            

while at_goal() != True:
    if wall_in_front() and wall_on_right():
        turn_left()
        while right_is_clear() != True or at_goal() == True:
            if wall_in_front():
                turn_left()
            else:
                move()
                if at_goal():
                    done()
    elif right_is_clear():
        if front_is_clear():
            turn_right()
            move()
        elif right_is_clear():
            turn_right()
            move()
    else:
        move()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
        
# MAZE SOLUTION    
while at_goal() != True:
    if wall_in_front() and wall_on_right():
        turn_left()
        while right_is_clear() != True or at_goal() == True:
            if wall_in_front():
                turn_left()
            else:
                move()
                if at_goal():
                    done()
    elif right_is_clear():
        if front_is_clear():
            turn_right()
            move()
        elif right_is_clear():
            turn_right()
            move()
            
    else:
        turn_left()