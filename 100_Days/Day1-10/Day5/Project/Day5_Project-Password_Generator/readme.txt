Project 5 - password Generator

###--- PROJECT OBJECTIVES ---###

The objective of this project is to create a rudimentry password generator that will take inputs to generate a password from the provided lists
Below the base code has been provided to solve the effort of manually typing it all out. Our objective is below

---------------------------------------------------------------------------------------------

COPY THIS CODE:

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

---------------------------------------------------------------------------------------------

Objective one // easy level - Create the code needed to fit the following criteria
# 4 letters, 2 symbol, 2 number // NON RANDOMIZED
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


Objective one // hard level - Create the code needed to fit the following criteria
# 4 letters, 2 symbol, 2 number //RANDOMIZED
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
