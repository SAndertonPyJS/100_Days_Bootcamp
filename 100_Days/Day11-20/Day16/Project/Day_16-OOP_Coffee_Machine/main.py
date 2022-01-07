#!usr/bin/env/python

### --- IMPORTS --- ###

#here are our class imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#we want our clear function
from os import system, name
#time too
import time

### --- SETUP --- ###

#first we want to setup our classes
drink = Menu()
makeit = CoffeeMaker()
money = MoneyMachine()

### --- Functions --- ###

#as always we want a clear console func
def clear():
    """clears the console
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

### --- MAIN --- ###

#so we want to setup a while loop as per last time to ensure we can keep running the machine
dispense = True

while dispense:
    greet = input(f"What would you like today?: {drink.get_items()}: ").lower()
    #we want to tie our drink choice to a variable to prevent retyping and access attributes
    choice = drink.find_drink(greet)
    if greet in drink.get_items():
        #first we check our resources if it's enough for our drink
        #feed our drink name -> into find drink func -> argument for resource check
        resource_check = makeit.is_resource_sufficient(drink.find_drink(greet))
        #if sufficient
        if resource_check == True:
            #we have the machine make a payment based on our drink and return change / True if it is enough
            payment = money.make_payment(choice.cost)
            if payment == True:
                #finally if the payments true we then make the coffee
                makeit.make_coffee(choice)
    elif greet == 'report':
        makeit.report()
    elif greet == 'off':
        print("Shutting down for maintainence. Goodbye")
        time.sleep(1)
        dispense = False
        clear()

#currently the program has us run a loop because it wants us to keep using the machine until it runs out of
#resources in an always on state instead of shutting down on a fail to refill, to that end i kind of tweaked
#the resources to ensure it can run for awhile before needing to be reset