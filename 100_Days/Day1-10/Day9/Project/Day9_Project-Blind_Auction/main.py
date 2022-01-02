#!usr/bin/env/python

### --- IMPORTS --- ###

#we want the art 
from art import logo
#import os for clear
from os import system, name


### --- VARIABLES --- ###

#we want a dict of our bidders so we create here to store later
bidders = {}
#we want to create this to kill our while loop later
finished = False

### --- FUNCTIONS --- ###

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#we want to create a basic function to deal with the info we get from the user here
def bids(name, amount):
  #this adds the name and amount into the dict
  bidders[name] = int(amount)

#now we create a function to determine the winning bid
def winning_bid(bidders):
  #create a highest bid container for our loop
  highest_bid = 0
  #create a winner variable to call later
  winner = ''
  #loop through our bids dict, checking the value of each key.
  for bidder in bidders:
    #bid amount = current bidder name / number being checked
    bid_amount = bidders[bidder]
    #if currently being checked is highest?
    if bid_amount > highest_bid: 
      #replace the highest with current amount
      highest_bid = bid_amount
      #replace name with current key (name)
      winner = bidder
  #after we're done print the winner
  print(f"The winner is {winner} with a bid of ${highest_bid}")


### --- EXECUTABLES --- ###

#now for while loop as we want more than one participant
while not finished:
  #if more bidders:
  print(logo)
  print("Welcome to the secret auction.")
  name = input("What is your name?: ")
  amount = input("How much would you like to bid?: ")
  bids(name, amount)
  again = input("Are there anymore bidders? Type Yes or No: ").lower()
  #endloop:
  if again == 'no':
    #kill it
    finished = True
    #announce winner
    winning_bid(bidders)
  #continueloop:
  elif again == 'yes':
    clear()










  
