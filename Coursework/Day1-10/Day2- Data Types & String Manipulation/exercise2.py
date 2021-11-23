#first we get the weight and height in float because decimals

weight = float(input("what is your weight in kg?: "))
height = float(input("what is your height in m?: "))

#then we round our formula down (bmi formula being weight * height squared)

bmi = round(weight / (height * height))

#now we print bmi

print(f"Your BMI is {bmi} ")