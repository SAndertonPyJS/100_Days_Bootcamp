#for this exercise we need to replicate fizzbuzz, fizzbuzz is as follows;
    # if number diviible by 3 print fizz instead of number
    # if number divisible by 5 print buzz instead of number
    # if number divisible by 3 and 5 print fizzbuzz instead of number

#so first we want to setup our loop
for number in range(1, 101):
    #now we want if statements first to prevent confusing the program we want 
    #our 3 and 5 conditional first:
    if number % 3 == 0 and number % 5 == 0:
        #if the number divisible by 3 and 5 print fizzbuzz
        print("Fizzbuzz")
    elif number % 3 == 0:
        #if divisible by 3 fizz
        print("Fizz")
    elif number % 5 == 0:
        #if 5 buzz
        print("Buzz")
    else:
        #else print number
        print(number)
