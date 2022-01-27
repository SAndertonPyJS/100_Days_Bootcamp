#!usr/bin/env/python

#Use dict comprehension to convert the values in the key value pair to farenheit

#our temps
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

#now to comprehension

#we loop through weather c, and leave days the same but for the temp in every entry we apply
#the fatenheit formula
weather_f = {day:temp *9/5 +32 for (day, temp) in weather_c.items()}
print(weather_f)