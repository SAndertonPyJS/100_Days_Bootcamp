#!usr/bin/env/python

### --- IMPORTS --- ###

#we want to import tkinter
from tkinter import *
#we want to import messagebox to create a messagebox (not a class so seperate import)
from tkinter import messagebox

### --- WINDOW SETUP --- ###

#setup our window object
window = Tk()
#window title
window.title("Password Manager")
#we want to config the window 
window.config(padx=20, pady=20)

#Now we want to create a canvas on the image
canvas = Canvas(width=200, height=200)
#get our lock image
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
#now we want to add it to the grid
canvas.grid(row=0, column=1, columnspan=2)

### --- FUNCS --- ###

#we want to make an additional function here, this is my own addition to the code, will enable user to
#cycle textboxes with tab instead of having to manually click on each one
def focus_next_window(event):
    """Allows us to focus the next textbox widget with tab for user friendliness

    Args:
        event ([type]): event passed through from the .bind() method on the textboxes
    """
    event.widget.tk_focusNext().focus()
    return("break")

#now we want a function to save the passwords and information
def save_info():
    """Function that gathers the info in the entryboxes, confirms information, checks missing information
        and writes to a text file. Then empties the boxes
    """
    website = website_textbox.get()
    user = user_textbox.get()
    password = password_textbox.get()


    #we want to also check if the fields have been filled correctly
    if len(password) == 0 or len(website) == 0 or len(user) == 0:
        messagebox.showinfo(title="Error", message="Missing text in field(s) please make sure you have entered correct information")
    else:
        #we want to confirm these details
        is_ok = messagebox.askokcancel(title=website, message=f"These are the provided details: \nUser: {user} " 
                                               f"\nPassword: {password} \nAre these correct?")
        if is_ok:
            #we now want to write the info to a file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                #now we delete the entries
                website_textbox.delete(0, END)
                user_textbox.delete(0, END)
                password_textbox.delete(0, END)
                #finally focus website box
                website_textbox.focus()
        else:
            pass

#now for the last part of the project, we want to get the password generator function to work.
def generate_password():
    """Generates a password on button press of password generate
    """
    #We're actually going to make this easier and steal / reformat our old code from day 5. The password generator project.
    #its been heavily refactored using what we know about list comprehension
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_l = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_s = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_n = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    #a list of the three lists from above
    password_list = pw_l + pw_n +pw_s

    #shuffle the list
    random.shuffle(password_list)

    #turn it into a string
    password = "".join(password_list)

    #finally we populate the entry
    password_textbox.insert(0, password)

### --- LABELS / BUTTONS / TEXT BOXES / UI --- ###

#website label and textbox
website_label = Label(text="Website")
website_label.grid(row=1, column = 0)
website_textbox = Entry(width=35)
website_textbox.grid(row=1,column=1,columnspan=3,sticky=EW)
#we do focus here to ensure cursor is focued on this field when the app opens
website_textbox.focus()
website_textbox.bind("<Tab>", focus_next_window)

#username / email textbox and label
user_label = Label(text="Username/Email")
user_label.grid(row=2, column = 0)
user_textbox = Entry(width=35)
user_textbox.grid(row=2,column=1,columnspan=3,sticky=EW)
user_textbox.bind("<Tab>", focus_next_window)

#password_label / textbox / password generation button
password_label = Label(text="Password")
password_label.grid(row=3, column = 0)

#or label
or_label = Label(text=" or   ")
or_label.grid(row=3, column =2, sticky=W)

password_textbox = Entry(width=25)
password_textbox.grid(row=3,column=1,sticky=W)
password_textbox.bind("<Tab>", focus_next_window)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3,column=3,sticky=EW)
#we want to create a lambda function here, with no event so that it will invoke the addbutton 
#when we hit return
window.bind("<Return>", lambda event=None: password_button.invoke())  

#finally we want an add button to add it to our passwords
add_button = Button(window, text="Add", command=save_info)
add_button.grid(row=4, column=0,columnspan=4, sticky=EW)
#we also create a lambda here for the add
window.bind("<Return>", lambda event=None: add_button.invoke())  

### --- MAIN CODE --- ###



### --- MAINLOOP --- ###

#we want to keep it running
window.mainloop()