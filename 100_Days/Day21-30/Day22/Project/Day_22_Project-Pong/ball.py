#!usr/bin/env/python

### --- IMPORTS --- ###

#grab our Turtle module for inheriting
from turtle import Turtle

### --- CLASS --- ###

#creating our class, inheriting from turtle
class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.create_ball()
        
    def create_ball(self):
        """Creates teh ball
        """
        self.color("white")
        self.shape("square")
        self.penup()
        #initial movement angles
        self.x_move = 3
        self.y_move = 3   

    def move(self):
        """Moves the ball
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Changes y coord on collision
        """
        self.y_move *= -1

    def bounce_x(self):
        """Changes X coord on collisionX
        """
        self.x_move *= -1
    
    def reset(self):
        """Resets the ball, and changes the starting direction
        """
        self.goto(0, 0)
        self.bounce_x()
