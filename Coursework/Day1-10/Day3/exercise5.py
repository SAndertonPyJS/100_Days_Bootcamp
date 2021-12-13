#For this exercise we need to build a love calculator that will calculate "love"
#in reality the idea is to use if /else statements to see how many times the letters
#true love appears in each string and then add them together to form a %

#first we want the names and we want to make them lower case to unsure no input issues
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

#to make this easier we will combine the two names into one string

combined_name = name1 + name2

#next we want a variable for both true and love to count occurances count unfortunately
#only takes 3 inputs so we need to do it like this:

#there must be a better way to do this pepehands
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

true = t + r + u + e
love = l + o + v + e

#we now want to make this a score number by adding them together, but we can't just
#add them together we need to make them a string

#will render our '%'
true_love = int(f'{true}{love}')
#will do basic addition (we don't want this)
#true_love_int = true + love

#now to our if / else statement

if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}. You go together like coke and mentos.")
elif true_love >= 40 and true_love <=50:
    print(f"Your love score is {true_love}. You are alright together.")
else:
    print(f"Your love score is {true_love}.")



