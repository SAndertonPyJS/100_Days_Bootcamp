#!usr/bin/env/python

### --- IMPORTS --- ###

#we need turtle for inheriting 
from turtle import Turtle

### --- CLASSES --- ###

class Borders(Turtle):
    #we want to create a border class here to add white top and bottom borders
    def __init__(self, position) -> None:
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=128)
        self.penup()
        self.goto(position)

        
class Middle_Break(Turtle):
    #this will add a dashed line in the middle of the screen
    def __init__(self) -> None:
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.setheading(270)
        self.penup()
        self.goto(0,360)
    
    def draw_line(self):
        """Draws a line down the middle of the arena
        """
        for i in range(100):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)
            