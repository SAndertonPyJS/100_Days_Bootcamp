#Reeborgs world solving. 
#The following code is to solve the four hurdles challenges in https://www.reeborgsworld.ca
#They are designed to test knowledge of definitions and while loops
#To note for the final one the hurdle size/ height / distance from goal is random so we must account for this.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    #we start our hurdle jump turning left
    turn_left()
    #keep moving up the wall until there is no wall
    while wall_on_right() == True:
        move()
    #execture right turn to get over the wall and turn again to begin moving down
    turn_right()
    move()
    turn_right()
    #move down until you meet ground
    while front_is_clear() == True:
        move()
    #turn left
    turn_left()
        
#then we repeat

#set up our final loop, if theres a wall execute jump, else keep moving.
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#this accounts for both the lack of ability to A. Turn right, and B. Hop the hurdle. 

#With A it's as simple as doing a 270 degree turn to go right so 3x turn_left(). 
#B is a tad harder as we need to determine is there a wall on right, is the front clear 
#and when to move when to turn. Using two while loops solves this problem. This also satisfies all other maze modes.