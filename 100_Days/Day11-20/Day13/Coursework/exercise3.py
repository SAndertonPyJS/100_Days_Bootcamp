for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

# There were 3 major bugs here, lack of elif, an or statement and [] inside print. The lack of elif meant that the number + fizz or buzz would have been printed, 
# the or statement meant that instead of looking for the specific 3 and 5 it would do either or. Finally the []was making the numbers be printed as list items. 

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)