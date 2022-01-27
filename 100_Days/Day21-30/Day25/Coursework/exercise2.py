#!usr/bin/env/python

### --- IMPORTS --- ###

import pandas

### --- MAIN --- ###

#first we want to get our data

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#we now want to get the primary fur color

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

#next we want to create a dict to encapsulate this data

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]

}

#testing
print(squirrels_dict)

#now we use pandas ability to make dataframes out of it and turn it into a csv

squirrel_df = pandas.DataFrame(squirrels_dict)
squirrel_df.to_csv("squirrel_count.csv")