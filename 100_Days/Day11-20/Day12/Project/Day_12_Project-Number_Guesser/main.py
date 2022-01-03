### --- IMPORTS --- ###

#we want random to get random numbers ect
import random
#we want time to deal with resetting stuff and slowing down processes
import time
#we want these for our clear func
from os import system, name

### --- VARIABLES / LOGO --- ###

# Include an ASCII art logo.
logo = '''
 _   _                 _               
| \ | |               | |              
|  \| |_   _ _ __ ___ | |__   ___ _ __ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |   
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                       
                                       
 _____                                 
|  __ \                                
| |  \/_   _  ___  ___ ___  ___ _ __   
| | __| | | |/ _ \/ __/ __|/ _ \ '__|  
| |_\ \ |_| |  __/\__ \__ \  __/ |     
 \____/\__,_|\___||___/___/\___|_|     
                                       
'''

print(logo)

#computer generates a random number (currently set at 10 for testing purposes)
computer_number = 10

#we want trackers for turns remaining, whether we have failed or not and numbers guessed
turns = 0
alive = True
numbers_guessed = []

### --- FUNCTIONS --- ###

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

#we want a reset func for starting over
def reset():
    """resets console after game is over
    """
    print("Goodbye")
    time.sleep(3)
    clear()

### --- GAME SETUP --- ###

#The project guidelines wanted us to include difficulty (difficulty being number of starting turns)

#we want to give them the choice
difficulty = input("Select a difficulty: Easy or Hard: ").lower()

#if difficulty easy give 10 turns and let them know
if difficulty == 'easy':
    turns += 10
    print(f"You have selected easy mode, turns: {turns}, good luck!")
#else if it's hard 5 turns let them know
elif difficulty == 'hard':
    turns += 5
    print(f"You have selected hard mode, turns: {turns}, good luck!")
#finally this is here for error handling and user feedback, if they don't enter the correct things will let them know and end program
else:
    print("Sorry invalid selection friend! Goodbye")
    alive = False
    reset()

### --- MAIN --- ###

#while loop to keep the game going while we guess
while alive == True:
    #if we have more turns
    if turns > 0:
        #guess the number
        guess = int(input("What do you think the number is? (between 1 and 100): "))
        #Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
        if guess > computer_number:
            print("Too High")
            # Track the number of turns remaining.
            turns -=1
            #add the number to the guesses
            numbers_guessed.append(guess)
            #print remaining turns and currently guessed
            print(f"You have {turns} turns remaining")
            print(f"Numbers currently guessed: {numbers_guessed}")
        elif guess < computer_number:
            print("Too Low")
            turns -=1
            numbers_guessed.append(guess)
            print(f"You have {turns} turns remaining")
            print(f"Numbers currently guessed: {numbers_guessed}")
        # If they got the answer correct, show the actual answer to the player.
        else:
          print(f"That's it chief the number was in fact {computer_number}")
          alive = False
          reset()

# If they run out of turns, provide feedback to the player. 
if turns == 0:
    print("You have run out of turns, thanks for playing!")
    alive = False
    reset()





