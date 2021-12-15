#password generator project

###--- IMPORTS ---###
import random

###--- LISTS FOR PW ---###

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

###--- INPUTS ---###

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

###--- MAIN ---###

#first we will want to set a variable called password to contain the characters

password = ""

#now we wanna loop through our lists and pull random letters/numbers/symbols from each
#then decare that random choice to a variable which we add to the password

for n in range(1, nr_letters+1):
    letter = random.choice(letters)
    password += letter
for n in range(1, nr_symbols+1):
    symbol = random.choice(letters)
    password += symbol
for n in range(1, nr_numbers+1):
    number = random.choice(letters)
    password += number

#easy challenge complete a password with 0 randomization

print(f"You wanted {nr_letters} letters, {nr_symbols} symbols and {nr_numbers} numbers. Your final password is: {password}")

#for the hard challenge we want to dive a bit deeper and use join / random sample

#.join takes multiple items and joins them together as a string (opposite of split)
#sample will take the string we have created and randomly take one of each item from the string

#this piece of code is saying to join the randomly selected parts of the string from
#password into a new random string. If we print it now we will still have the same 
#amount of letters / numbers / symbols just randomized.
random_password = ''.join(random.sample(password, len(password)))

print(f"Here is the password. But randomized: {random_password}")