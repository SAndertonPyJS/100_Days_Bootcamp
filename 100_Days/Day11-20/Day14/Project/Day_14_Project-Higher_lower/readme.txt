### --- HIGHER LOWER GAME --- ###

Todays project is the higher lower game, or a basic version of it, the idea is that the
user is presented with two options and have to then choose between them.

The choice they have to make is, is the number count of object 2 higher or lower,
if they successfully choose they get a point, if they fail the game ends. 

With that in mind:

Structure:

WE are provided with 3 files starting out, the art, game data and our main file.

The art contains the logo and vs ascii art for the program
The game data contains the data for the people we will compare (a list of dicts)
The main file is where we will write code and is currently empty.  


### --- FLOW --- ###

The program should (and this can double as project directives to prevent retyping)

Greet the user
   -> Display the logo, Display data 1, vs and data 2
        -> From here it will ask higher or lower
        -> user needs to be able to input higher or lower as an input
            -> the program will check data 2 vs 1 to see if it is higher or lower
                -> if failure, announce it was wrong end the game
                -> if success computer will take data 2, change it to data 1 variable
                -> load a new data value for 2 and then ask again
                    -> repeat process until user fails
                    -> tally score
                    -> end game