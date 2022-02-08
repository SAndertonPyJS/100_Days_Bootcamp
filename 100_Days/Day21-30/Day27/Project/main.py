#!usr/bin/env/python

### --- IMPORTS  --- ###

#we want to import tkinter 
from cgitb import text
from tkinter import *


### --- FUNCS --- ###

#we only need one function, to convert and edit the label we are using
def convert():
    """Converts the specified number to km

    Args:
        num ([type]): the number needed for converting
    """
    #we need to get the miles input
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometers_result_label.config(text=km)

### --- WINDOW SETUP --- ###

window = Tk()
window.title("Miles to Kilometer Converter")

### --- GRID STUFF --- ###

#OUR INPUT

#we want a window to enter our miles
miles_input = Entry()
#and we want to add it to the grid
miles_input.grid(column=1, row=0)

#OUR TEXT LABELS

#miles label
miles_label = Label(text="mi")
miles_label.grid(column=2, row = 0)

#is equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

#km result label 
kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

#km label
kilometers_label = Label(text="km")
kilometers_label.grid(column=2, row=1)

#BUTTONS

#calculate button
calculate_button = Button(text="Calculate", command = convert)
calculate_button.grid(column=1, row=2)

### --- EXIT/MAINLOOP --- ###

window.mainloop()
