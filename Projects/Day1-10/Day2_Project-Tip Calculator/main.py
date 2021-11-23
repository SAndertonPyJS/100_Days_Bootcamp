#welcome our guests
print("welcome to the tip calculator!")

#ask how much the bill was
bill = float(input("How much was your bill? $"))

#ask tip also user proof, tell them explicitly what it wants, we want a number in string form we can concatinate to the "1." so it can be turned into a float
tip = float("1." + (input("What % of tip did you leave? (Number only Between 1-99 (No Symbols / letters)): ")))

#next calculate the bill
bill_w_tip = round(float(bill * tip) , 2)

#finally ask for number of people dining
number_people = int(input("How many people were dining?: "))

#and calculate!

bill_p_p = round(float(bill_w_tip / number_people), 2)

print(f"Your bill was: ${bill}, with tip the total bill was ${bill_w_tip} and you dined with {number_people} people, your final bill per person comes to: ${bill_p_p}")