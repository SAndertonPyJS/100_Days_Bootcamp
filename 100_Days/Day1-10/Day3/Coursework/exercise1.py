#WE need to create a piece of code that calculates if an integer is odd or even 

#first an input to get the number from the user
number = int(input("Please enter a number: "))

#next we do the main calculation. even numbers will always be divisible by 2 with a 0
#remainderso we use modulo we can then setup our conditionals with this in mind

#even
if number % 2 == 0:
    print(f"Your chosen number was {number}. This is an EVEN number.")
#if it's not even it's obviously odd
else:
    print(f"Your chosen number was {number}. This is an ODD number.")



