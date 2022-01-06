#!usr/bin/env/python

### --- IMPORTS --- ###

#import our clear func
from os import system, name
#importing random so we can choose a random piece of data / time for stalling
import random, time

### --- STARTING CODE --- ###

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

### --- FUNCS --- ###

#as always we want a clear console func
def clear():
    """
    clears the console
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check_resources(ingredients):
    """Loops through the item vs resources if resources are less that well == not enough and we end transaction

    Args:
        ingredients ([type]): The ingredients of the variable passed through
    """
    #loop through each item in ingredients
    for item in ingredients:
        #if at any point not enough
        if ingredients[item] >= resources[item]:
            #print this
            print(f"Sorry there is not enough {item}")
            #kill loop (remember loops are default as true)
            return False
    #if it manages to get through all ingredients, we have enough, return true and continue
    return True
    
def process_coins():
    """Has user insert coins for their order, and then tallies the total
    """
    print("Please insert coins:")
    #ask for how many of each and add them
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def check_transaction(payment_given, drink_cost):
    """Return true if there's enough money, false if not

    Args:
        payment_given ([type]): Money recieved from process coins fun
        drink_cost ([type]): cost of the drink variable 
    """
    #we want to global profit to ensure the profit is added for later use
    global profit
    #if payment not enough
    if payment_given < drink_cost:
        print("Sorry not enough money was given for this drink, Money refunded")
        return False
    #if enough
    else:
        profit += drink_cost
        change = round(payment_given - drink_cost, 2)
        print(f"Transaction accepted. Here is your ${change} change. Printing Receipt")
        return True

def make_coffee(drink_name, ingredients):
    """Makes the coffee and deducts resources

    Args:
        drink_name ([type]): Name of the drink being made
        ingredients ([type]): ingredients of the drink being made
    """
    #loops through the ingredients and deducts from resources
    for item in ingredients:
        resources[item] -= ingredients[item]
    #confirm to user drink is being made
    print(f"Here is your {drink_name}")

### --- MAIN --- ###

dispensing = True

while dispensing:
    greet_order = input("Welcome, please select a coffee [Espresso | Latte | Cappuccino]: ").lower()
    if greet_order == "off":
        dispensing = False
    elif greet_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[greet_order]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(greet_order, drink['ingredients'])
        else:
            print("Please contact a member of staff for a refill!")
            dispensing = False
            time.sleep(2)
            clear()

