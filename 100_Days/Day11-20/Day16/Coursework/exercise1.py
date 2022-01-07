#!usr/bin/env/python

### --- IMPORTS --- ###

#we want to install pypi for this coursework intro. Not included in the github upload is the Venv we will be using
#i'll be using venvs (mainly to build habit) to largely create environments for any package that isn't standard with python
from prettytable import PrettyTable

#as we did in the coursework before, we want to create / initialize the object by tying it to a variable
table = PrettyTable()

#so by reading the documentation we know we can take the objects method and properties and use them with our new variable

table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Charmander", "Fire"],
        ["Bulbasaur", "Grass"],
        ["Squirtle", "Water"],
        ["Pikachu", "Electric"]
    ]

)

table.align = 'l'

print(table)