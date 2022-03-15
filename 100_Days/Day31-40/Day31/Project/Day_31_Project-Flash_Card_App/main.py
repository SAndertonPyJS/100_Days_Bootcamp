#!usr/bin/env/python

### --- IMPORTS --- ###

#we want to import everything from tkinter
from tkinter import *
#import pandas to read data for our cards
import pandas
#we also want random so we can randomly select data
import random

### --- CONSTANTS --- ###

#bg color for the app
BACKGROUND_COLOR = "#B1DDC6"
#setup a current card global for our functions
current_card = {}
#a to learn variable for the try and except data
to_learn = {}

### --- READ CSV DATA --- ###

#we need to check and see if theres a words to learn csv. If there isn't we do nothing and load french words. Good old try/except

try:
    #we want to read it with pandas
    french_words = pandas.read_csv("./Day_31_Project-Flash_Card_App/data/words_to_learn.csv")
except FileNotFoundError:
    original_word_list = pandas.read_csv("./Day_31_Project-Flash_Card_App/data/french_words.csv")
    to_learn = original_word_list.to_dict(orient="records")
else:
    to_learn = french_words.to_dict(orient="records")

### --- FUNCTIONS --- ###

#we create our functions here for the buttons

def next_card():
    """Gets random french word for the card and adds it to flash card. On button press moves to next card
    """
    #we global current card so that it can update to the main one, and then future functions don't need extra lines written
    global current_card, flip_timer
    #we get the random card to add to current card
    current_card = random.choice(to_learn)
    #now we add the word to the card
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    #we want to change the card back to french side in case it flipped
    canvas.itemconfig(card_background, image=card_front_img)
    #we want the card to flip after 3 seconds, so user can see what the word is
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    """Gets random french word for the card and adds it to flash card. On button press moves to next card and removes the learnt word from to_learn
    """
    #for this we want to remove the current card
    to_learn.remove(current_card)
    #we also want to create a csv of words to learn for next time we open the app
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Day_31_Project-Flash_Card_App/data/words_to_learn.csv", index=False)
    #then call the next card
    next_card()
    

def flip_card():
    """Flips the card to the english version, changing the color of the card and text and swapping to the english translation
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

### --- SCR SETUP --- ###

#tkinter window
window = Tk()
window.title("Flash Card Study For Serious Gamers")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#we want the card to flip after 3 seconds, so user can see what the word is
#we tie this to a variable so we can continuously abuse it during function calls
flip_timer = window.after(3000, func=flip_card)

#create our canvas
canvas = Canvas(width=800, height=526)
#we want a front image and a back image for the front and back of the card
card_front_img = PhotoImage(file="Day_31_Project-Flash_Card_App/images/card_front.png")
card_back_img = PhotoImage(file="Day_31_Project-Flash_Card_App/images/card_back.png")
#we now create the background for the card
card_background = canvas.create_image(400, 263, image=card_front_img)
#next we want two blank text pieces that will be filled later on witht hese fonts
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
#we want the background color to be filled 
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
#finally we grid it
canvas.grid(row=0, column=0, columnspan=2)

### --- BUTTONS --- ###

#now we create our buttons for the check and cross
cross_image = PhotoImage(file="Day_31_Project-Flash_Card_App/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="Day_31_Project-Flash_Card_App/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

### --- MAINLOOP --- ###

#we want to call a card before mainloop so that title word doesn't appear at the start
next_card()

window.mainloop()