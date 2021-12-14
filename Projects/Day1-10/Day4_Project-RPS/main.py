#!usr/bin/env/python

### --- IMPORTS --- ###

import random

### --- ASCII ART ---###

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

### --- MAIN --- ###

#first we want to take our ascii art and put them into a list 
possible_choices = [rock, paper, scissors]
#then we want to create a list of all possible user choices
user_choices = [0, 1, 2]

#next we want to ask the user what to pick 
user_choice = int(input("Please enter A number 0:Rock, 1:Paper, 2:Scissors, take note no other numbers will work:"))

#now for our first conditional, we want to make sure what the user picked was valid
if user_choice not in user_choices: 
    #if they didn't pick 0, 1 or 2
    print("Your choice was not a valid number, please choose again")
else:
    #do our game
    #we let the computer choose a random number of the possible user choices, seeing as the user can only pick from that we let the cpu do too.
    cpu_choice = random.choice(user_choices)
    #now that both player and cpu have picked we compare

    #The best way to figure out who won is by greater than / less than, then in the case of one picking rock vs one picking scissors we can
    #do a specific condition for that. So we need: draw, 1 vs 2, 2 vs 3 and finally 1 vs 3

    #first the draw condition:
    if user_choice == cpu_choice:
        print(f"CPU chose {cpu_choice}, {possible_choices[cpu_choice]} User chose {user_choice}, {possible_choices[user_choice]}ITS A DRAW!")
    #next we want to code up the rock vs scissor condition, thought scissor is a greater number on the list than rock it SHOULD lose.
    #user gets scissors and cpu gets rock
    elif user_choice == 2 and cpu_choice == 0:
        print(f"CPU chose {cpu_choice}, {possible_choices[cpu_choice]} User chose {user_choice}, {possible_choices[user_choice]}CPU WINS!")
    #user gets rock, cpu gets scissors
    elif user_choice == 0 and cpu_choice == 2:
        print(f"CPU chose {cpu_choice}, {possible_choices[cpu_choice]} User chose {user_choice}, {possible_choices[user_choice]}USER WINS!")
    #now the rest of our conditions, user greater than
    elif user_choice > cpu_choice:
        print(f"CPU chose {cpu_choice}, {possible_choices[cpu_choice]} User chose {user_choice}, {possible_choices[user_choice]}USER WINS!")
    #finally user less than
    else:
        print(f"CPU chose {cpu_choice}, {possible_choices[cpu_choice]} User chose {user_choice}, {possible_choices[user_choice]}CPU WINS!")


    




    

