### --- Project --- ###

Automated Birthday Wisher

### --- WHAT WE NEED --- ###

-SMTP
-Pandas
-Datetime

### --- STEP BY STEP PROCESS --- ###

1/ We use datetime to get the current day of the year
2/ Then we get pandas to compare the date to the list of birthdays on record
3/ If it matches - WE read open both the letter templates (and pick a random one) as well as the name of the person attached to the birthdays
4/ WE then use mailmerging to merge it into a finished letter/message
5/ And send it with SMTP