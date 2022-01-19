#!usr/bin/env/python

### --- IMPORTS --- ###

#we want turtle to make our object
from turtle import Turtle

### --- CLASS --- ###

#gonna super this
class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.create_paddle()
        self.speed("fastest")
        self.goto(position)

    def create_paddle(self):
        """Creates the paddle for the game
        """
        self.shape("square")
        self.shapesize(stretch_wid=5.5, stretch_len=1)
        self.color("white")
        self.penup()

    def move_paddle_up(self):
        """Moves our paddles up, ensuring they can't go out of bounds
        """
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        
    def move_paddle_down(self):
        """Moves the paddles down ensuring they cannot go out of bounds
        """
        if self.ycor() > -270:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)