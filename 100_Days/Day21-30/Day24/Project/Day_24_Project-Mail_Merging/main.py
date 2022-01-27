#!usr/bin/env/python

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

### --- CONSTANTS --- ### 

#first we want to get ahold of our text we are replacing

PLACEHOLDER = "[name]"

### --- OPEN FILES --- ###

#let's open our invited list
with open("./Input/Names/invited_names.txt") as names_file:
    #we want to use readlines to read every line individually
    names = names_file.readlines()

#now the starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    #we only want to read this as a whole
    letter_contents = letter_file.read()
    #now let's loop throuhg the names and replace the name
    for name in names:
        #we want to strip the \n from each of the names in the name file
        stripped_name = name.strip()
        #we want to create a new letter of replaced names
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #now we want to nav to ready to send and place our new letters
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            #write the new letter to the location
            completed_letter.write(new_letter)