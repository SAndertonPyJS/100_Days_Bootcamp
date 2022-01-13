#!usr/bin/env/python

#Exercise create an etch a sketch with turtle using what you have leared about higher order
#fucntions and event listeners

#The only parameters to note are:
# Move forward with W, Backward with S, counter-clockwise is A and clockwise is D

### --- IMPORTS --- ### 

#first we get turtle
from turtle import Turtle as T
from turtle import Screen as S

### --- SETUP TURTLE --- ###

t = T()
s = S()

### --- FUNCTIONS --- ###

#we now create a function for each movement action to tie to the listeners later

def move_forward():
    """Function that moves turtle object forward
    """
    t.forward(10)

def turn_left():
    """Function that turns the turtle left
    """
    t.left(10)

def turn_right():
    """Function that turns turtle right"""
    t.right(10)

def backward():
    """Function That moves turtle backward"""
    t.backward(10)

### --- EVENT LISTENERS --- ###

#we tell the screen to start listening
s.listen()

#now we assign our keys to each function, we don't need () as we don't want to call 
#functions on a specific line but rather only to trigger when we entter a key press

s.onkey(key="w", fun=move_forward)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="s", fun=backward)

### --- EXIT --- ###

#our exit process
s.exitonclick()