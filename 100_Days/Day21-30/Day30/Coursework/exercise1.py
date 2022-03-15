### --- PROVIDED CODE --- ###

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)

### --- SOLUTION --- ###

#TODO: Catch the exception and make sure the code runs without crashing.

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    #we use try a except index error here. IT tries to get the 4th index of fruit pie
    #which is usually out of range. So if it ends up throwing that error it will instead
    #print fruit pie instead of erroring out.
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

#if we change the amount to within range it will instead trigger the try/ else
make_pie(4)