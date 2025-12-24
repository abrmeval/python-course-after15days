def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def go_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

 
def move_forward():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        move()
    
def move_forward_height():
    if wall_in_front() and wall_on_right():
        turn_left()        
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_right()
        move()

def walk():
    if wall_in_front():
        if right_is_clear():
            turn_right()
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()
    
while not at_goal():
    walk()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
