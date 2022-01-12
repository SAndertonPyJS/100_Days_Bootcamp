#!usr/bin/env/python

### --- IMPORTS --- ###

from turtle import Screen, Turtle as T, color
import random

### --- INITIALIZE THE TURTLE --- ###

#make our boi
t = T()

#create a screen
screen = Screen()

### --- CHALLENGES --- ###

#1 -> Draw a square
def draw_square():
    """Uses a for loop to automate drawing a square with minimal lines of coding
    """
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)

#------------------------------------------------------------#

#2 -> Draw a dashed line  
def draw_dashed_line():
    """Uses a for loop to draw a dashed line
    """
    for i in range(30):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)

#------------------------------------------------------------#

#3 -> Draw multiple different shapes

def draw_shapes(start, end):
    """Function to make the turtle create shapes of varying sidess

    Args:
        start ([type]): Starting shape sides
        end ([type]): Ending shape sides
    """
    #choose our colors
    colors = ["paleturquoise", "seagreen", "firebrick", "darkseagreen", "chocolate", "crimson", "moccasin"]
    #our number of sides is equal to the start and the end provided +1
    total_sides = range(start, end+1)

    #now we enumerate turning total_sides into an object we can loop through (otherwise would throw an error)
    for i, sides in enumerate(total_sides):
        #we set the color to the current integer, aka our range enumarate
        color_choice = colors[i]
        #chooses colors
        t.color(color_choice)
        #moves and turns according to the current i
        for i in range(sides):
            t.forward(100)
            t.right(360/sides)

#------------------------------------------------------------#

#4 -> Random walk

def walk():
    """Makes the turtle do a random 500 step walk, each time changing color and direction
    """
    #we want to make a turn we can call on
    turn = [0, 90, 180, 270]
    colors = ["paleturquoise", "seagreen", "firebrick", "darkseagreen", "chocolate", "crimson", "moccasin"]
    t.pensize(20)
    t.speed(15)
    for i in range(150):
        col_choice = random.choice(colors)
        t.color(col_choice)
        t.forward(30)
        t.right(random.choice(turn))

#------------------------------------------------------------#

def spirograph():
    """Makes turtle draw a spirograph
    """
    #first we want our colors
    colors = ["paleturquoise", "seagreen", "firebrick", "darkseagreen", "chocolate", "crimson", "moccasin"]
    #now we want it to do circles, we can use a loop + a set turn for every circle
    t.pensize(1)
    t.speed(30)
    for i in range(0, 360, 2):
        t.color(random.choice(colors))
        t.circle(100)
        t.right(2)
### --- CHALLENGES_RESOLVED --- ###

#uncomment the func to see it in action. 

#1
#draw_square()
#2
#draw_dashed_line()
#3
#draw_shapes(3, 10)
#4
#walk()
#5
#spirograph()

### --- END --- ###

screen.exitonclick()