#using the math function and basic functions we want to create a piece of code that will tell us the number
#of cans of paint required to paint a wall


### --- IMPORTS --- ###

# step 1 rounding up, we can't use round as it's not 100% accurate so we use math and math.ciel to round up: 
import math


### --- FUNCTION --- ###

#create our paint calc function with height, width, cover as arguments
def paint_calc(height, width, cover):
  #our number of cans is equal to upper rounding of our width * height / amount a can can cover
  number_of_cans = math.ceil((width * height) / cover)
  #print our number of cans
  print(f"You will need {number_of_cans} of paint")
  
### --- MAIN --- ###

#inputs
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
#how much one can can cover
coverage = 5
#do our function with arguments
paint_calc(height=test_h, width=test_w, cover=coverage)


