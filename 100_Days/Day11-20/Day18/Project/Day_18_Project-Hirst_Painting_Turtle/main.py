#!usr/bin/env/python

### --- IMPORTS --- ###

#we want to install colorgram, and import it (with venv) to extract our colors
import colorgram
#now we get trutle
from turtle import Screen, Turtle as T
#we want random colors
import random

### --- TURTLE --- ###

t=T()
screen = Screen()
#important! needs to be set to 255 color to be able to utilize rgb values
screen.colormode(255)
#testing for better visibility
#screen.bgcolor("black")

#we want some settings
t.penup()
t.hideturtle()
t.speed("fastest")
t.setposition(-200, 0)

### --- FUNC --- ###

def get_colors():
    """Gets the colors from the image.jpg in the folder
    Returns:
        [type]: Returns a list of all the rgb colors in tuple format
    """
    rgb_colors = []
    #extract 30 occurances of color from the image
    colors = colorgram.extract('image.jpg', 30)
    #loop through the colors and take the rgb values (and not the labels)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        #make a color tuple out of it
        new_color = (r, g, b)
        #add it to the list
        rgb_colors.append(new_color)
    #return the list
    return rgb_colors



### --- MAIN --- ###

#we want to set our x coord to -100 so that it doesn't go off screen
x = -100
#will loop through a range and each time set turtles position to new coords pain dot, move on
for _ in range(10):
    #starting pos -200, x (x starting at -100)
    t.setposition(-200, x)
    #loop for each line of dots
    for _ in range(10):
        #choose the color, put the penup, move, pendown
        t.dot(20, random.choice(get_colors()))
        t.penup()
        t.forward(50)
    #add to the x coord and repeat
    x += 50

#exit
screen.exitonclick()