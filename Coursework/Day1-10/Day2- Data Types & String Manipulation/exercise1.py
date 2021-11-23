#get a number input needs to be a string so that we can take 0 / 1 from string positions

number = input("Please input a two digit number for us to add together!: ")

#now we convert each string piece to an int

number1 = int(number[0])
number2 = int(number[1])

#Add them together

final_number = number1 + number2

#Print

print(f"Adding your numbers now! {number1} + {number2} equals {final_number}")