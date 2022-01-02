#!usr/bin/env/python

### --- IMPORTS --- ###

#we add our logo for the top of the program
from art import logo
#import time to wait as needed
import time
#import os for clear
from os import system, name

#print logo
print(logo)

### --- VARIABLES --- ###

should_continue = True

#first number we want to account for floats incase decimals
number_1 = float(input("Input number: "))
#our choice of the operator
user_choice = input("Choose an operator [+] [-] [/] or [*]: ")
#second number
number_2 = float(input("input number: "))

### --- FUNCTIONS --- ###

#We create a function that will do our operation based on the choice
def calculation(n1, n2):
  if user_choice == '+':
    return n1 + n2
  elif user_choice == '-':
    return n1 - n2
  if user_choice == '*':
    return n1 * n2
  if user_choice == '/':
    return n1 / n2

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#now we want to calc our number and return an answer
answer = calculation(number_1, number_2)
#print the answer formatted for user 
print(f"{number_1} {user_choice} {number_2} = {answer}")

#ask if they want to go again
go_again = input("Continue Calculation, Y or N?: ").lower()

#now we set an empty variable for a second number
answer2 = 0

#if user wants to continue
while should_continue == True:
  #if yes repeat
  if go_again == 'y':
    #new number is asked for
    new_number= float(input("Pick another number: "))
    #do operation
    user_choice = input("Choose an operator [+] [-] [/] or [*]: ")
    #answer 2 is calculation of original answer, and new number
    answer2 = calculation(answer, new_number)
    #print for users
    print(f"{answer} {user_choice} {new_number} = {answer2}")
    #reassign the new answer to old answer
    answer = answer2
    #repeat
    go_again = input("Continue Calculation, Y or N?: ").lower()
  #if no don't repeat
  elif go_again == 'n':
    print("Goodbye")
    should_continue = False
    time.sleep(3)
    clear()
