#!usr/bin/env/python

### --- IMPORTS --- ###

#create our class for the actual quiz background mechanics
class QuizBrain:
    #create our init
    def __init__(self, q_list) -> None:
        """Init for QuizBrain

        Args:
            q_list ([type]): Question list that will come from the question bank
        """
        #default question number starts at 0 (counting from 0)
        self.question_number = 0
        #we want to create an attribute that takes an input
        self.question_list = q_list
        #we want to keep track of score here
        self.score = 0

    #we want to create a method to continue asking questions
    def next_question(self):
        """Takes the current question in the question list and presents it to the user 
            with an input option
        """
        #we want the question, so we tell it to search the list with the index of the question number
        current_question = self.question_list[self.question_number]
        #we want to increase question number to access new questions + can fix the q.0 bug :)
        self.question_number +=1
        #we want the user_answer here
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. True/False?: ")
        self.check_answer(user_answer, current_question.answer)
    
    #We want to create a method that will check the list to see if there are questions
    #left and if there are it will return true
    def still_questions(self):
        """Returns True while question list is smaller than the length of question_list
        """
        return self.question_number < len(self.question_list)

    #we now want to create a means to check an answer against the question answer

    def check_answer(self, user_answer, question_answer):
        """Checks the answer vs the user answer

        Args:
            user_answer ([type]): Answer inputted by the user in next_question()
            question_answer ([type]): question answer from data.py
        """
        if user_answer.lower() == question_answer.lower():
            print("Correct")
            self.score +=1
        else:
            print("Incorrect")
            print(f"The correct answer was {question_answer}")
        


