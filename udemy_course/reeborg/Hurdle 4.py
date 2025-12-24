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
    if wall_in_front():     
        turn_left()
        move()
    else:
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    
while not at_goal():   
    move_forward_height()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
