#First we want to get an input age

your_age = int(input("How old are you?: "))

#next we subtract that from 90 

remaining_years = 90 - your_age

#now we get the d/w/m (remaining years * by how many of each in a year)

day_left = remaining_years *365
week_left = remaining_years * 52
month_left = remaining_years * 12

#Finally print, for testing ex output at 56 years is
#You have 12410 days, 1768 weeks, and 408 months left.

print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left.")