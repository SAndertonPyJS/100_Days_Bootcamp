# we have our numbers

a = 3
b = 5

#printing so we have a control to test against

print(f"a is equal to {a}")
print(f"b is equal to {b}")

#----------------#

#we store a in a new variable c, then store b in a, and finally store c in b
#the result being c =3, a=5, b=3 we end up with a c variable unused but complete the objective
c = a 
a = b
b = c

#print final objective
print("Swapping numbers now!")
print(f"a is now equal to {a}")
print(f"b is now equal to {b}")