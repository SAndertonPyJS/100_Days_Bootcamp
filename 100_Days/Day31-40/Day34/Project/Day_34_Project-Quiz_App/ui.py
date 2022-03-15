#!usr/bin/env/python

#D34: We're building a quiz UI class with tkinter

### --- IMPORTS --- ###

#import tkinter to make gui app
from tkinter import *
#import quizbrain to get our questions for gui app
from quiz_brain import QuizBrain

### --- CONSTANTS --- ###

THEME_COLOR = "#375362"

### --- CLASS --- ###

class QuizInterface:
    #we want our ui class init, we pass in quiz_brain from main.py and give it the QuizBrain data type
    def __init__(self, quiz_brain: QuizBrain) -> None:
        """Init for the TKinter window
        """
        #we put out quizbrain here 
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #score label to keep track of correct answers
        self.score_label = Label(text="Score: 0",fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        #canvas where the main text will be shown
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",15,"italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #the images for true / false buttons
        true_image = PhotoImage(file="Day_34_Project-Quiz_App/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, sticky=W)

        false_image = PhotoImage(file="Day_34_Project-Quiz_App/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, sticky=E)

        #we call teh next question here
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets the next question and displays it on the screen
        """
        #we want to stop index error
        if self.quiz.still_questions():
            #if questions left go to next question
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            #we get our text from next question
            q_text = self.quiz.next_question()
            #then we edit the text
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            #if quiz over we want to disable buttons and display end / score
            self.canvas.itemconfig(self.question_text, text=f"Quiz Complete\nYour Score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Takes the button input and feeds it into the give feedback func
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Takes the button input and feeds it into the give feedback func
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Gives feedback to the user in form of bg changes

        Args:
            is_right (bool): bool fed in from either true pressed / false pressed
        """
        #change the color based on right / wrong
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        #gets next question after 1 second
        self.window.after(1000, self.get_next_question)
        
