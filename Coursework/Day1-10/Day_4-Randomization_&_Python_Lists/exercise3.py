#For this exercise we will use  lists to create a treasure map
#this treasure map will act in a 0, 1, 2 x 0, 1, 2 grid.

#step 1, get our row and columns from position
#step 2, place our X
#step 3, error handling / bad inputs, this is a bonus I want to add something to prevent errors arising if 
#the user places a wrong number into the position input

###--- Imports ---###

#First we want random
import random

###--- Main ---###

#This is the code provided from exercise start hree rows that contain white boxes, 
#the idea is to write some code that will replace a random one of these with an X our three rows
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
#our 'map' a list of the three lists
map = [row1, row2, row3]
#this print statement just visualizes our 'map'
print(f"{row1}\n{row2}\n{row3}")

#this input will ask us where we want to put the treasure, the two digit number is our coords
#the first digit represents the vertical column number the second is row number
#we need to remember list index starts at 0 so when we enter the digits they start counting from 0 not 1
position = input("Where do you want to place treasure? Enter two digits between 0-2 ex 01, 00, 21 or 20 ect: ")

##STEP 3: finally we want some error handling. 

#we create a list of the possible combinations 
possible_numbers = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]

#then an if statement to control the main code block, if the user enters a number not in the possible combinations
#the code does not execute and instead prints to try again. 
if position not in possible_numbers:
    print("The number you have chosen isn't valid please try again")
else:
    #here are our row and column variables
    ##STEP1:
    row = int(position[1])
    column = int(position[0])

    #pretty much what this does is go to position[1] in map list and replace the list item at position[0] with X
    ##STEP2:
    map[row][column] = "X"



    #This will print the updated rows
    print(f"You want to place tour treasure at {position}? Then so it shall be")
    print(f"{row1}\n{row2}\n{row3}")