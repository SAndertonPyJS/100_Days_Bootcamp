###########DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# The big is that range goes from 1 - 20 but does not include 20, i will never == 20 FIX: range must be (1, 21)

#########################################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# The bug is we will never get 1 as in programming we count from 0, so rand int counting from 1-6 has two issues, 1/ it will never catch 1 as 1 in this range is 2 and 2/ it will sometimes fail as it will look for index 6 which doesn't exist. FIX: randint(0, 5)

#########################################

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# The bug is that if 1994 is entered nothing will happen, as we only have less than or greater than 1994 so we need to ammend it. 
# FIX: if year > 1980 and year <= 1994:

#########################################

# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

# The bug is that print is not tied to the if statement, so even if under 18 will still print, there is also an issue that nothing else will print if another age is inputted and that the f statment is missing in the print.

# FIX:
# age = input("How old are you?")
# if age >= 18:
#   print(f"You can drive at age {age}.")
# else:
#   print(f"You are {age}, you are too young to drive.")

#########################################

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# The bug is that words_per_page has == instead of = so it's not being assigned the input but rather it's trying to check it. as a result words_per_page = 0 and total_words becomes 0

# FIX: word_per_page = int(input("Number of words per page: "))

#########################################

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# The bug is that the b_list.append(new_item) is outside the for loop as a result it will only append the last item. FIX: put it inside the loop.