#In this exercise we will create a piece of code to loop through a list of student scores
#and find the highest using loops

#first we want to get our scores, using split again
student_scores = input("Input a list of student scores ").split()

#now we want to make a variable to contain the highest score
highest_score = 0

#now loop through our list, n being the list item
for n in range(0, len(student_scores)):
    #make our list items integers
    student_scores[n] = int(student_scores[n])
    #now to contain our highest score we want to be able to compare the current highest
    #to our new number, and then later we don't want it overwritten. So we use an if here
    if student_scores[n] > highest_score:
        #if the score currently being looped through is higher
        highest_score = student_scores[n]
        #we replace the highest score with that student score
    
    else:
        #do nothing
        pass

    #this means that while looping it will encapsulate the highest score it finds, then
    #check against that score, if it finds no other score higher, well we have our highest

#finally print   
print(f"The scores submitted were {student_scores} the highest score was {highest_score}")