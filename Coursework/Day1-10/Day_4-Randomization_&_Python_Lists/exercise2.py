#For this exercise we are going to create a piece of code that takes the names of everyone entered
#then chooses randomly between them to pay for a bill. The main stipulation is to find a way without
#doing the random.choice func

###--- Imports ---###

#first random
import random

###--- Main ---###

#next we want to get the names inputted, we can do it all in one input and use string.split to 
#remove the commas and put them in a list, string.split removes whatever character is specified in a string.

#get our names
names_string = input("Give me everybody's names, separated by a comma. ")
#split our names, and remove the comma, as this results in multiple pieces of data it stores names as a list
names = names_string.split(", ")

#testing
#print(names, type(names))


#from here we put our random into play, we can't use choice, so instead we will get the length of the names list
#and then pick a random number from that

who_pays = random.sample(names, 1)

#testing
#print(who_pays)
#print(who_pays[0])

#Now we come to our final statement

print(f"{who_pays[0]} will pay the bill today!")