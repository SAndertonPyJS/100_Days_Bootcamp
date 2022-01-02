def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    while front_is_clear() != True:
        turn_left()
    move()
    if right_is_clear():
        turn_right()

# Reebog.ca maze puzzle solution, simple when thought out maze exit is always somewhere on the right, 
# so we needed to setup a loop that basically said keep going till you get there, if front is clear, 
# turn right move if front is not clear turn left till it is.
