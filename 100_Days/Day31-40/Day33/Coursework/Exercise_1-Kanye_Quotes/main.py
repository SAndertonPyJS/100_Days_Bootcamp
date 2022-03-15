### --- IMPORTS --- ###

#we want the tkinter gui for our gui
from email.quoprimime import quote
from tkinter import *
# requests to get our kanye quotes
import requests

### --- REQUEST --- ###

def get_quote():
    """Get's the kanye quote and returns it for use in the tkwindow
    """
    request = requests.get("https://api.kanye.rest")
    request.raise_for_status()
    data = request.json()
    #we set the actual text of the quote to quote variable
    quote = str(data["quote"])
    #finally we want to edit the canvas text
    canvas.itemconfig(quote_text, text=quote)

#testing
#print(get_quote())

### --- MAIN --- ###

#window setup here
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

#we want to setup our canvas here, bg, kanye img and the text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Exercise_1-Kanye_Quotes/background.png")
canvas.create_image(150, 207, image=background_img)
#the quote text is the constant
quote_text = canvas.create_text(150, 207, text="kanye quotes appear here", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

#finally we want to add the button, as well as the command to change the quote (get_quote)
kanye_img = PhotoImage(file="Exercise_1-Kanye_Quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()