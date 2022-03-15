#!usr/bin/env/python

### --- IMPORTS --- ###

#D34: We're importing HTML to deal with unescaping HTML
import html

### --- CLASS --- ###

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
        self.current_question = self.question_list[self.question_number]
        #we want to increase question number to access new questions + can fix the q.0 bug :)
        self.question_number +=1
        #D34: To facilitate dealing with unescaping HTML we're gonna add this line here
        q_text = html.unescape(self.current_question.text)
        #D34: we want to return the question text/ answer to put it on the gui
        return f"Q.{self.question_number}: {q_text}"
    
    #We want to create a method that will check the list to see if there are questions
    #left and if there are it will return true
    def still_questions(self):
        """Returns True while question list is smaller than the length of question_list
        """
        return self.question_number < len(self.question_list)

    #we now want to create a means to check an answer against the question answer

    def check_answer(self, user_answer):
        """Checks the answer vs the user answer

        Args:
            user_answer ([type]): Answer fed in by the user in next_question()
        """

        #sets correct answer to the current answer
        correct_answer = self.current_question.answer
        #if user answer is true add score return bool 
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            return True
        #else return bool
        else:
            return False



