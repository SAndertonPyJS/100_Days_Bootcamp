#!usr/bin/env/python

#Use list comprehension to filter even numbers

#our list of numbers
numbers = [1,2,3,4,5]

#in this example we tell the comprehension to only include the number if it's able 
#to cleanly modulo 2 with 0 left over the result is the filtered even numbers
filtered_numbers = [n for n in numbers if n%2 == 0]
print(filtered_numbers)