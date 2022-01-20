#!usr/bin/env/python

### --- IMPORTS --- ###

from turtle import Turtle
#import random for random car color
import random

### --- CONSTANTS --- ###

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

### --- CLASS --- ###

class CarManager():
    def __init__(self) -> None:
        #we want a list to contain our cars
        self.all_cars = []
        #these are movement options we want to manipulate to make it harder later
        self.move_distance = 5
        self.move_increment = 10
        #this method creates our inital turtles
        self.create_car()

    def create_car(self):
        """Create the car (turtle) and add it to the list
        """

        #we need a random chance so it doesn't spawn a wall of cars
        random_chance = random.randint(1,6)
        #if it rolls 6 spawn a car
        if random_chance == 6:
            #our car settings
            new_car = Turtle("square")
            #make it rectangle
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            #random choice of the colors
            new_car.color(random.choice(COLORS))
            #set it's y axis, we have to skew the number abit as it's always 25px off on once side
            random_y = random.randrange(-200, 225, 25)
            #send it to starting pos and append
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        #loop through list and start moving the cars
        for car in self.all_cars:
            car.backward(self.move_distance)
        



