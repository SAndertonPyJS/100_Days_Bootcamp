#!usr/bin/env/python

### --- IMPORTS --- ###

#turtle for inheriting
from turtle import Turtle

### --- CONSTANTS --- ###

FONT = ("Courier", 20, "bold")

### --- CLASS --- ###

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        #our settings for the score turtle 
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed('fastest')
        self.score_point()

    def score_point(self,):
        """Changes the score based on if ball went out of bounds
        """
        #clear current score
        self.clear()
        #go to score position
        self.goto(-230,270)
        #set our message
        self.message = f"LEVEL: {self.score}"
        #write the message
        self.write(self.message, move=False, align="center", font=FONT)
    
    def add_score(self):
        """Increases the score by 1
        """
        self.score +=1

    def game_over(self):
        """Prints game over on the screen
        """
        #go to middle
        self.goto(0,0)
        #set our message
        self.message = "GAME OVER"
        #write the message
        self.write(self.message, move=False, align="center", font=FONT)