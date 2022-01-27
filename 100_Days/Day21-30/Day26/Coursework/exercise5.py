#!usr/bin/env/python

#Use dict comprehension to turn a sentence into a list of key value pairs
#the key should be the word, the value should be the len of the word

#our sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow"


#now our dict comprehension
#we tell the comprehension to create a dictionary for each word
#with the key being word, the value being len for each word in the sentence
#we also split the sentence into different strings.
word_dict = {word:len(word) for word in sentence.split()}
print(word_dict)