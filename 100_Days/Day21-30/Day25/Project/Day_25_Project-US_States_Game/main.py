#!usr/bin/env/python

### --- IMPORTS --- ###

#here's our turtle
import turtle
#here's our pandas
import pandas


### --- SCREEN SETUP --- ###

#we want to setup the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

### --- DATA --- ###

#we want our data to be readable
data = pandas.read_csv("50_states.csv")
#we want to convert it to a list so we can check contents in an if statement
all_states = data.state.to_list()
#list of guessed states, we can use it to count total correct and also to control our while loop
guessed_states = []
#D26.CW - removed missing states list to add it later for list comprehension

print(all_states)

### --- MAIN --- ###

#while loop to keep guessing
while len(guessed_states) < 50:
    #get our user input
    answer_state = screen.textinput(title=f"{len(guessed_states) }/50 Correct", prompt="What's antoher state's name").title()

    #we want to create an exit function
    if answer_state == "Exit":
        #if user exits, append all missing states to a new list, for converting to csv later
        #D26.CW - changed for loop to a list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        #now we pandas it into a dict and csv.
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        #now break the loop
        break
    
    #check if the answer is in the list 
    if answer_state in all_states:
        #add our answer to the guessed list
        guessed_states.append(answer_state)
        #if it's corrrect we create a turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #we get the state data 
        state_data = data[data.state == answer_state]
        #now we tell it to go to that state
        t.goto(int(state_data.x), int(state_data.y))
        #now write the state
        t.write(answer_state)


### --- EXIT --- ###

#we don't want it to exit right away
turtle.mainloop()