#!usr/bin/env/python

### --- IMPORTS --- ###

#were importing turtle for inheritance

from turtle import Turtle

### --- CONSTANTS --- ###

SCORE_FONT = ('Arial', 100, 'bold')
ALIGNMENT = 'center'


### --- Class --- ###

class Scoreboard(Turtle):
    #our settings for the score turtle 
    def __init__(self, position) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(25,25,25)
        self.speed('fastest')
        self.score_point(position)

    def score_point(self, position):
        """Changes the score based on if ball went out of bounds
        """
        #clear current score
        self.clear()
        #go to score position
        self.goto(position)
        #set our message
        self.message = self.score
        #write the message
        self.write(self.message, move=False, align=ALIGNMENT, font=SCORE_FONT)
    
    def add_score(self):
        """Increases the score by 1
        """
        self.score +=1