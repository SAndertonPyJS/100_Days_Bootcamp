#using if / else statements we want to check if a year is leap or not

#The working formula for figuring out a leap year is as follows
#on every year that is evenly divisible by 4 **except** 
#every year that is evenly divisible by 100 **unless** 
#the year is also evenly divisible by 400

#so let's get a year

year = int(input("Please enter a year: "))

#if the year is cleanly divisible by 4 (modulo)
if year % 4 == 0:
    #then it's leap
    print(f"{year} is a leap year")
    #HOWEVER if it's also divisible by 100 it is not a leap year
    #we wanna check all conditions so using if again
    if year % 100 == 0:
        print(f"{year} is not a leap year")
        #finally we want to actually catch 400s, because it can be divisible by 4 and 100
        #but not 400 so any 400's are also leaps
        if year % 400 == 0:
            print(f"{year} is a leap year")
        #well if it' not divisible by 400 deffo not leap
        else:
            print(f"{year} is not a leap year")
    #this will catch all the divisible by 4's but not centuries aka 1984
    else:
        print(f"{year} is a leap year")
#finally if it can't even be divided by 4 it's obviously not a leap year
else:
    print(f"{year} is not a leap year")

#we can also condense it a bit by getting rid of the first two prints

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")