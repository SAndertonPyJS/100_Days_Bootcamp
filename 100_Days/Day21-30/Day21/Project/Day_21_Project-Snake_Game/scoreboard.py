#!usr/bin/env/python

### --- IMPORTS --- ###

#were importing turtle for inheritance

from turtle import Turtle

### --- CONSTANTS --- ###

SCORE_FONT = ('Arial', 12, 'bold')
ALIGNMENT = 'center'

### --- CLASS --- ###

class Scoreboard(Turtle):
    #let's init our score
    def __init__(self) -> None:
        super().__init__()
        #setting for the actual score
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.score_point()
        

    def score_point(self):
        """Changes the score based on food collected
        """
        #clear current score
        self.clear()
        #go to score position
        self.goto(0, 280)
        #set our message
        self.message = f"Score: {self.score}"
        #write the message
        self.write(self.message, move=False, align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        """Generates the game over message
        """
        #go to middle of screen
        self.goto(0, 0)
        #write our game over message
        self.write("Game Over", align=ALIGNMENT, font=SCORE_FONT)
    