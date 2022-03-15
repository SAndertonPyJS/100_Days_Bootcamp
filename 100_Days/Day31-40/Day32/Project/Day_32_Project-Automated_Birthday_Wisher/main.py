### --- IMPORTS --- ### 

#we want datetime for our datetime
import datetime as dt
#we want smtp to send emails
import smtplib
#import pandas for our reading of csv
import pandas
#we want random to choose a random letter
import random

#### --- SETTING TIME --- ###

#first we need the day, we get this by creating a now variable and tapping into that for the day
now = dt.datetime.now()
#we want to set a tuple up that looks at the month / day for cross checking our birthdays
today = (now.month, now.day)
print(today)

### --- READING OUR CSV --- ###

#we read the data from the csv
birthday_data = pandas.read_csv("./Day_32_Project-Automated_Birthday_Wisher/birthdays.csv")
#then turn the data we want into a dict using comprehension
#the day and month for the data of day month in the csv iterrows
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

### --- MAIN EXECUTION --- ###
#now we check the day against the dict
if today in birthday_dict:
    #if a match get the name of that person
    birthday_person = birthday_dict[today]

    ### --- GET AND MERGE LETTERS --- ###

    #choose a random letter
    file_path = f"./Day_32_Project-Automated_Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        #merge the name with the birthday persons name
        contents = contents.replace("[NAME]", birthday_person["name"])


    ### --- EMAIL SETUP --- ###

    #we get our variables for our email login
    my_email = "learningtocodejspy@gmail.com"
    password = "E1x2i3l4u5s6!Shaun"

    #now we connect to the smtp lib
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=birthday_person["email"], 
        msg=f"Subject:Happy Birthday :D!\n\n{contents}")
    connection.close()