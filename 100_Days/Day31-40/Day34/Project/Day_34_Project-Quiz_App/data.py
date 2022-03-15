#!usr/bin/env/python

### --- IMPORTS --- ###

#we want to import requests here to get question data
from tkinter.messagebox import QUESTION
import requests

### --- CONSTANTS --- ###

#we want to set a constant for number of questions here so we can easily change later
QUESTION_AMOUNT = 10

### --- REQUEST --- ###

#parameters for the request
parameters = {
    "amount": QUESTION_AMOUNT,
    "type": "boolean",

}

#let's get our data
response = requests.get("https://opentdb.com/api.php", params=parameters)
#raise status for any errors
response.raise_for_status()
#and now our raw data in json format
data = response.json()
question_data = data["results"]



