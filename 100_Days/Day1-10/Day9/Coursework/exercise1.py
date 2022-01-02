
#we have the scores assigned in the exercise here
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#first we make an empty dictionary to hold our grades
student_grades = {}

#next we create a for loop that will loop through the dictionaries
for student in student_scores:
  #the loop is looking for the scores and will check the values of the student key
  score = student_scores[student]
  #if scores meet a certain criteria
  if score >= 91:
    #assign the student key the grade value in the grades dict
    student_grades[student] = "Outstanding"
  elif score >= 81 and score < 90:
    student_grades[student] = "Exceeds Expectations"
  elif score >= 71 and score < 80:
    student_grades[student] = "Acceptable"
  else: 
    student_grades[student] = "Fail"

#finally print our grades dictionary
print(student_grades)





