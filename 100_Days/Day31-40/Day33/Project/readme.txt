### --- PROJECT --- ###

The aim of this project is to create a small script that will email the user when the ISS is overhead and it's nighttime

### --- PARAMETERS / HOW IT WORKS --- ###

The program works as follows:

Firstly it get's the position of the user (the user provides these details)
Secondly it get's the current position of the ISS using the API
It then uses date time to get the current time of day based on the users coordinates

Finally it compares the data and if the time of day is night as well as the iss being within 5 degrees + or - 
of the users lat / long it will email the user using the smtplib module

### --- NOTES --- ###