# Step 1 let's redefine is_leap
def is_leap(year):
  #formula stays the same
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #however instead of is_leap we return true or false
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Step 2: New function to check the days
  #Function takes two arguments the year (aka year we are inputting for leapyear too)
  #and the month we want to check (as always start from 0 == january)
def days_in_month(year, month):
  #we create a list of all the days in every month with 28 in febuary
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  #now to satisfy the leap days requirement 
  if is_leap(year) == True:
    #if it's a leap year we reassign the febuary index to 29
    month_days[1] = 29
    #then we return the list as a variable / list for use later
    return month_days[month]
  #if it's not a leap we leave it alone and return the list
  elif is_leap(year) == False:
    month_days[1] = 28
    return month_days[month]
  
#we get the year variable from this input for using in functions
year = int(input("Enter a year: "))
#we get the month here
month = int(input("Enter a month: "))
#the days variable is the return of our new function so we want month 1 it will
#print febuarys day count based on the year
days = days_in_month(year, month)
print(days)












