#!usr/bin/env/python

### --- IMPORTS --- ###

#our classes and objects
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#our cleanup funcs
from os import name, system
import time

### --- SETUP --- ###

#first we create a question bank list
question_bank = []

#then we loop through each question in the question data
for question in question_data:
    #we take the text and answer and add them to a variable
    question_text = question["text"]
    question_answer = question["answer"]
    #we then create an object for each text and answer as a question
    new_q = Question(q_text=question_text,q_answer=question_answer)
    #then append it to the question bank
    question_bank.append(new_q)

### --- ADDITIONAL FUNCS --- ###

#as always we want a clear console func
def clear():
    """clears the console
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

### --- OBJECTS --- ### 

#we now create a new QuizBrain object and use the questionbank as our qlist
quiz = QuizBrain(question_bank)

### --- MAIN --- ###

while quiz.still_questions():
    quiz.next_question()

time.sleep(1)
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
time.sleep(2)
print("Goodbye")
time.sleep(2)
clear()

