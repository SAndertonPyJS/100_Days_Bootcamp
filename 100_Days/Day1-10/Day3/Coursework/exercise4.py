#using the below and a host of if statements we need to calculate the price of a pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

#rules of the pizza:
    # Small Pizza: $15
    # Medium Pizza: $20
    # Large Pizza: $25
    # Pepperoni for Small Pizza: +$2
    # Pepperoni for Medium or Large Pizza: +$3
    # Extra cheese for any size pizza: + $1


#first we want to create a variable to track the price

price = 0

#if size is == (chosen size) add to pizza price
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
else:
    price += 25

#next we add pepperoni:
    #HOWEVER cost is dependant on size

#peperroni on small
if add_pepperoni == 'Y' and size == 'S':
    price += 2
#peperroni on med /large
elif add_pepperoni =='Y' and size == 'M' or size == 'L':
    price +=3
#no peperroni == do nothing
else:
    pass

#finally extra cheese:
if extra_cheese == 'Y':
    price +=1
else:
    pass

print(f"Order: {size} pizza, pepperoni: {add_pepperoni}, extra cheese: {extra_cheese}")
print(f"Final bill: ${price}")


    

