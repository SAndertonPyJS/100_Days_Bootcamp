#!usr/bin/env/python

### --- IMPORTS --- ###

#turtle for inheriting
from turtle import Turtle, position

### --- CONSTANTS --- ###

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

### --- CLASS --- ###

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        #all our init attributes here, we're making turtle in a method for now
        self.create_player()

    def create_player(self):
        """Create our turtle

        Args:
            position ([type]): The position we start at
        """

        #settings
        self.shape("turtle")
        self.color("white")
        #set it's heading so it's facing north at start
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the turtle north
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset(self):
        """Resets player position
        """
        self.goto(STARTING_POSITION)
