#!usr/bin/env/python

### --- IMPORTS --- ###

from turtle import Screen as S
from paddle import Paddle as P
from ball import Ball as B
from scoreboard import Scoreboard as Score
#an extras file to make it look nicer
from extra import Borders, Middle_Break

#we want time to prevent stuff going stupid fast
import time

### --- SCREEN SETUP --- ###


#setup our screen
scr = S()
scr.bgcolor("black")
scr.colormode(255)
scr.setup(width=1280, height=720)
scr.title("Pong")
scr.tracer(0)


### --- OBJECTS --- ###

#our paddles
r_paddle = P((612,0))
l_paddle = P((-620,0))

#our scoreboard
r_score = Score((250, -70))
l_score = Score((-250, -70))

#our extras
top_border = Borders((0, 355))
bot_border = Borders((0, -348))
middle = Middle_Break()
middle.draw_line()

#We want our ball
ball = B()


### --- LISTENERS --- ### 

#we need to get our paddles to move now
scr.listen()
#controls the right paddle
scr.onkeypress(r_paddle.move_paddle_up, "Up")
scr.onkeypress(r_paddle.move_paddle_down, "Down")
#controls left paddle
scr.onkeypress(l_paddle.move_paddle_up, "w")
scr.onkeypress(l_paddle.move_paddle_down, "s")


### --- MAIN --- ###

game_on = True
while game_on:
    time.sleep(0.0001)
    scr.update()
    ball.move()
    #Now we want to detect wall collisions:
    if ball.ycor() > 345 or ball.ycor() < - 338:
        ball.bounce_y()
    #now we want to detect paddle collisions:
    if ball.distance(r_paddle) < 30 or ball.xcor() > 660:
        ball.bounce_x()
    if ball.distance(l_paddle) < 30 or ball.xcor() < -660:
        ball.bounce_x() 
    #now we want to detect if a ball hits a goal / goes out of bounds
    if ball.xcor() > 650:
        time.sleep(.5)
        ball.reset()
        #finally we have scores:
        l_score.add_score()
        l_score.score_point((-250, -70))
    if ball.xcor() < -650:
        time.sleep(.5)
        ball.reset()
        r_score.add_score()
        r_score.score_point((250, -70))




















### --- EXIT --- ###

scr.exitonclick()