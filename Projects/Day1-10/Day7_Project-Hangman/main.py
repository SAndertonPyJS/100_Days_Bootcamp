### --- IMPORTS --- ###

#we want random to create a random word
import random
#we want to get the stages and log in from the art and the words in for the words
from hangman_art import stages, logo
from hangman_words import word_list

### --- VARIABLES --- ###

#We want to set a while loop conditional for later
end_of_game = False
#Select a random word from the word list
chosen_word = random.choice(word_list)
#Get the length of our chosen word for later
word_length = len(chosen_word)

#this will keep track of our lives
lives = 6
#WE add our guessed letters here to enable us to cross check later
letters_guessed = []

#print the logo :)
print(logo)

### --- TESTING --- ###

# print(f'The word is: {chosen_word}.')

### --- MAIN --- ###

#this is going to be the display we see when we have no letters
display = []
#we setup a for loop to generate the blanks with the same amount as our word
for _ in range(word_length):
    display += "_"

#while the game is on
while not end_of_game:
    #tell our user to guess a letter (ensure lower so that it does not raise errors)
    guess = input("Guess a letter: ").lower()
    #if the letter we want is already guessed
    if guess in letters_guessed:
      #give user feedback
      print(f"You have already guessed {guess}, please try again")
    
    #get the position of the letters we choose in word length
    #eg word is food, we guess d. This will find the position of d (3)
    for position in range(word_length):
      letter = chosen_word[position]
      #if letter is == to the guess (aka if it's in the word)
      if letter == guess:
        #change the blank to that letter
        display[position] = letter
        #add that letter to the guessed words list
        letters_guessed += guess
        
    # if it's not in the chosen word
    if guess not in chosen_word:
      #user feedback
      print(f"Sorry but {guess} isn't in the word, try again!")
      #remove a life and add letter to guessed letters
      lives -= 1
      letters_guessed += guess

    #If we run out of lives we must have lost
    if lives == 0:
      #kill the loop
      end_of_game = True
      #user feedback
      print("You lose")
    #print the word
    print(f"{' '.join(display)}")
    # if no blanks left you must have won
    if "_" not in display:
        #kill loop
        end_of_game = True
        #user feedback
        print("You win.")
    #print score (current stage based on remaining lives)
    print(stages[lives])

