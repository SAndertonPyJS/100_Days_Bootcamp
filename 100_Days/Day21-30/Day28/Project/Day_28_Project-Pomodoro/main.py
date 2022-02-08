#!usr/bin/env/python

#Create a pomodoro app using tkinter

### --- IMPORTS --- ###

#we want to import everything for tkinter
from tkinter import *
#we use math to get our count timer for formatting
import math

### --- CONSTANTS --- ###

#we want these constants for look, as well as timing
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
#we need to create a variable called reps to keep track of times completed
reps = 0
#we need a timer variable for when there's nothing happening and we reset
timer = None

### --- TKINTER WINDOW --- ###

#we want to create the tk window
window = Tk()
window.title("Pomodoro")
#we want to config the window 
window.config(padx=100, pady=50, bg=YELLOW)

### --- TIMER RESET --- ### 

def reset_timer():
    """Function to reset the app, it:
        - cancels the timer
        - sets the timer to 0
        - configs timer text
        - wipes checkmarks 
        - finally resets the reps.
    """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0

### --- TIMER MECHANISM --- ### 

def start_timer():
    """Function that starts the timer, we use it to set the timers as well
    """
    #global reps to keep track
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    
    #we need to set our timers and also change the text for better user experience

    #if odd reps work / reps == 0
    if reps %2 != 0 or reps == 0:
        count_down(work_sec)
        timer_label.config(text="Work",fg= GREEN)
    #if every 8th rep long break
    elif reps %8 == 0:
        count_down(long_sec)
        timer_label.config(text="Break",fg= RED)
    #if even reps but reps not on multiple of 8 short break
    elif reps %2 == 0 and reps %8 != 0:
        count_down(short_sec)
        timer_label.config(text="Break",fg= PINK)


### --- COUNTDOWN MECHANISM --- ### 

#we need to use what we learn about the after method for the countdown mechanism

def count_down(count):
    """Function to countdown the pomodoro timer, formats the fed in time into minutes:seconds then
    uses canvas.config and window after to call and change itself every second
    Args:
        count (int): starting countdown number 
    """
    #we get an error in display of seconds and mins at certain times, dynamic typing fixes this to keep a clock format
    count_min = math.floor(count / 60)
    #if less than 10 mins use dynamic typing to add a 0 in front
    if count_min <10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    #if seconds less than 10 add a 0 in front of it 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    #if seconds = 0 display it as 00
    if count_sec == 0:
        count_sec = "00"

    #configure canvas, set it as the count
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #set this statement to kill after if it's 0 time left
    if count > 0:
        #global our timer here to reset
        global timer
        #after allows us to call functions, at a set time, so tell it to call itself
        #also we tie it to a variable to cancel it in reset later
        timer = window.after(1000, count_down, count-1)
    #now we set an else statement to catch the 0, call the start_timer again
    else: 
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark_label.config(text=mark)
        
### --- UI --- ###

#and now this canvas item for the tomato, we use photoimage to set the tomato image on the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
#now we grid the canvas to the screen
canvas.grid(column=1, row=1)

#LABELS

#we want our timer text up top
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

#this is for our checkmarks we have no text as it will be updated as reps are added
check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

#BUTTONS

#our start and reset buttons to start the timers
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

### --- KEEP OPEN --- ###

#similar to turtle we use mainloop to keep it open
window.mainloop()
