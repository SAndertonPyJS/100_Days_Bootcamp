#!usr/bin/env/python 

#1/ Take the weather data csv and create a list out of it in exercise1.py
#Do this exercise using readlines, csv reader and pandas to see the difference in how much it takes to work

#first we use with
with open("./weather_data.csv") as data_list:
   data = data_list.readlines()

#testing
print(data)

#we want to remove new line characters

#this is an example of list comprehension essentially just a for loop but worded to fit on a single line
data = [x.strip() for x in data]
print(data)

print("----------------------------------------")

#we can also use the inbuilt csv reader

import csv
#1/ using with open and the csv reader method we can read the data as a list but also in rows
with open("./weather_data.csv") as data_list:
    data = csv.reader(data_list)
    #2/using an if and the for loop we take the row[1] (temps) and turn them into an int and append
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            degrees = int(row[1])
            temperatures.append(degrees)
    print(temperatures)

print("----------------------------------------")

#Finally another way to do this is via pandas

#not inbuilt using a venv
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])