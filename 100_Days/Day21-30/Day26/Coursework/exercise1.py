#!usr/bin/env/python

#Use list comprehension to square numbers

#our list of numbers
numbers = [1,2,3,4,5]

#our comprehension, we tell the code to multiply the n*n for each n in the list
#works exactly like a for loop, just in one line
squared_num = [n*n for n in numbers]
print(squared_num)