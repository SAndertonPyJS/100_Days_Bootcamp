#!usr/bin/env/python

### --- CLASS --- ###

#we create a new question class like so
class Question:
    #the question class will recieve the questions from data and as such
    #we want the init to take the text and answer arguments for us to model
    #the question
    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer

#testing
#new_question = Question("test", "false")
#print(new_question.text)
#print(new_question.answer)