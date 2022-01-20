#!usr/bin/env/python

### --- IMPORTS --- ###

#we want time for the refresh
import time
from tkinter import W

#our turtle imports
from turtle import Screen 

#our OOP imports
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

### --- SCREEN SETUP --- ###

#Screen setup
scr = Screen()
#gonna go and add a nice little bg :)
scr.bgpic("project/Day_23_Project-Turtle_Crossing/Crossing.png")
scr.setup(width=600, height=600)
scr.tracer(0)

### --- OBJECTS --- ###

player = Player()
score= Scoreboard()
cars = CarManager()

### --- LISTENERS --- ###

scr.listen()
scr.onkeypress(player.move, "w")


### --- MAIN --- ###

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    cars.create_car()
    cars.move_cars()

    #Detecting collision with goal zone
    if player.ycor() > 290:
        #score point
        score.add_score()
        score.score_point()
        #we also want difficulty to be a thing. Everytime turtle scores increase speed by 1
        cars.move_distance +=1
        player.reset()
        

        

    #detect car exiting map (we want to remove the excess) so they don't hog memory
    #the "cars" do not dissappear after we leave the screen, so they will keep going forever
    #and kill ram usage
    for car in cars.all_cars:
        if car.xcor() < -320:
            cars.all_cars.remove(car)
            car.reset()
            car.penup()
            car.goto(-400,-400)

    #detect player collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


### --- EXIT --- ###

scr.exitonclick()