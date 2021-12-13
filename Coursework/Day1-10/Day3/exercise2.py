#first we get the weight and height in float because decimals

weight = float(input("what is your weight in kg?: "))
height = float(input("what is your height in m?: "))

#then we round our formula down (bmi formula being weight * height squared)

bmi = round(weight / (height * height))

#next we want to return a select bmi based on the overall %

#over 35
if bmi > 35: 
    print(f"Your BMI is {bmi}. You are clinically obese.")
#Use elif here. Note about elif vs if:

#if will check all statements and feed back all that apply, elif will go through the
#code and only return the one that applies / stop after that

#greater than 30 or equal to 35 exactly
elif bmi > 30 or bmi == 35:
    print(f"Your BMI is {bmi}. You are obese.")

#over 25 or equal to 30
elif bmi > 25 or bmi == 30:
    print(f"Your BMI is {bmi}. You are slightly overweight.")

elif bmi >= 18.5 or bmi == 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")

#finally all else (we don't do else as we only intend for super low weight and a super
#high weight could still be triggered)
elif bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
