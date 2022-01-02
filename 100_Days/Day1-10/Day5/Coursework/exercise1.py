#WE need to write some code that will allow us to determine average heights over a range
#of heights inputted. TO do this we will use a for loop.

#First let's make a list from an input (split makes one piece multiple)
student_heights = input("Input a list of student heights ").split()

#next we create counters for later, as we cannot use sum OR len
total_height = 0
number_of_students = 0

#now we loop through the list
for n in range(0, len(student_heights)):
    #from here we turn each list item (n) into an integer
    student_heights[n] = int(student_heights[n])
    #now we want to calculate the average / number of students we add the height / +1
    #to them through each iteration
    total_height += student_heights[n]
    number_of_students += 1
#finally once the loop finishes we make an average student height variable for printing
average_height = round(total_height / number_of_students,2)
#and print
print(f"Your heights were {student_heights}, the number of students was {number_of_students} and the average height is {average_height}")
    