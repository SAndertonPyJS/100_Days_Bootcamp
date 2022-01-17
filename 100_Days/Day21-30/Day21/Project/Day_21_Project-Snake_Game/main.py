#!usr/bin/env/python

### --- IMPORTS --- ###

#our turtle stuff
from turtle import Screen as S

#import time for delays
import time

#import our snake
from snake import Snake
#import our food
from food import Food
#we also want our scoreboard
from scoreboard import Scoreboard

### --- SCREEN SETUP --- ###

#initialize screen object
scr = S()
#set the height and width
scr.setup(width=600, height=600)
#changes bg color
scr.bgcolor("black")
#adds a name to the top of the window
scr.title("Snake")
#tracer goes off so we can manually call movement
scr.tracer(0)

### --- OBJECTS --- ###

snake = Snake()
food = Food()
score = Scoreboard()

### --- LISTENERS --- ###

#we create listeners to control our boi
scr.listen()
scr.onkey(snake.up, "w")
scr.onkey(snake.down, "s")
scr.onkey(snake.left, "a")
scr.onkey(snake.right, "d")

### --- MAIN --- ###

#we want to setup a while loop
game_on = True
while game_on:
    #we want to delay and update the screen here
    scr.update()
    time.sleep(.2)
    #move our boi
    snake.move()
    #now we want to detect food collisions
    if snake.head.distance(food) < 15:
        #create a new piece of food
        food.make_food()
        #extend our snek
        snake.grow()
        #add to score
        score.score +=1
        score.score_point()

    #detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        #kill the loop
        game_on = False
        #trigger a game over
        score.game_over()

    #detect collision with tail, we loop through the segments past 0
    for segment in snake.segments[1:]:
        #if the snake distance is < 10 counts as collision kill the game 
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
        

















### --- EXIT --- ###

scr.exitonclick()