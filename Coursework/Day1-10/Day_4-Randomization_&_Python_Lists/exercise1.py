#Exercise 1 - Create a simple Heads or Tails executable using the random module

###--- Imports ---###

#first we import random
import random

###--- Main ---###

#now we want to tie random to a variable 
number = random.randint(0,100)

#finally we want to define heads or tails with if statements

if number <=50:
    print("Heads")
else:
    print("Tails")