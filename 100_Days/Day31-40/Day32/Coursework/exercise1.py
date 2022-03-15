### --- IMPORTS --- ### 

#we want datetime for our datetime
import datetime as dt
#we want smtp to send emails
import smtplib
#import random for random line selection
import random

#### --- SETTING TIME --- ###

#first we need the day, we get this by creating a now variable and tapping into that for the day
now = dt.datetime.now()
day = now.weekday()

### --- GETTING OUR MESSAGE --- ###

#we want to read the quotes file and grab a random quote for the email
lines = open('./Day_32_Project-Automated_Birthday_Wisher/quotes.txt').read().splitlines()
message =random.choice(lines)

### --- EMAIL SETUP --- ###

#we get our variables for our email login
my_email = ""
password = ""

#if day == 0 (monday)
if day == 0:
    #now we connect to the smtp lib
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email, to_addrs="", msg=f"Subject:Here is your monday motivational quote :)\n\n{message}")
    connection.close()
else:
    print("It's not monday mate. No quote sent.")