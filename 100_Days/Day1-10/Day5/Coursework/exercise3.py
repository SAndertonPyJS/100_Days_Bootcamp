#This exercise requires us to write a piece of code that adds all the numbers from 1 - 100
#inside a for loop.

#first let's make a variable to hold total numbers

total_even = 0

#next we want to setup our loop

for n in range(1, 101):
    #now we need to figure out how to select ONLY even. Thankfully modulo exists
    #we can use an if statement with modulo 2 to get all even numbers
    if n % 2 == 0:
        total_even += n
    #tldr if 2 fits into n evenly with 0 left over it's obviously even so we add it
    #to the total

#at the end print
print(f"The total even numbers between 0 - 100 is {total_even}")