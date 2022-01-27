#!usr/bin/env/python

#Use list comprehension to filter duplicate numbers from both files

#our list of numbers
numbers = [1,2,3,4,5]

#first for this we need to open each file

with open("./exercise3/file1.txt") as file1:
    file_1_data = file1.readlines()

with open("./exercise3/file2.txt") as file2:
    file_2_data = file2.readlines()

#now we do some list comprehension (remember can be done on non lists too)

#this will filter numbers that are in both files
filtered_numbers = [int(n) for n in file_1_data if n in file_2_data]
print(filtered_numbers)

