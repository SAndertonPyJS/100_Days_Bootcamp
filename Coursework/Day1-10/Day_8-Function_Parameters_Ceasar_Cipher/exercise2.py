#Create a code snippet to enable user to check if a number is prime

### --- FUNCTION --- ###

#step1: make the function
def prime_checker(number):
  #we want a variable to check against for our if statements later
  is_prime = True
  #we check every number between 2 and our number, (0 and 1 arn't prime) 
  for test in range(2, number):
    #we now test, if the current loop number is not our number and divides evenly with 0 left over it's not prime
    if number % test == 0:
      #so we swap is prime to false      
      is_prime = False 
    #don'e need an else as we're only checking for one thing. Then finally we print statements based on our number
    if is_prime:
      print("it's a prime number")
    else:
      print("not a prime")



### --- MAIN --- ###
n = int(input("Check this number: "))
prime_checker(number=n)



