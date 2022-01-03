### --- NUMBER GUESSER --- ###

The project for today is a small number guesser game/ program
The objective of the game is to correctly guess the number within the given turns to win

With that in mind:

### --- PARAMETERS --- ###

Our program needs to be able to ->
	Greet users
	Ask a user difficulty option (ez or hard)
	Adjust the settings based on that choice
	Randomly give a number to the player to guess 
	As players input guesses, check the guess vs the number ->
		if the number is too high or low let them know -> remove a life -> print guesses/lives remaining/ask again
		if number is correct let them know and complete game
		if you run out of turns/ lives, let them know end game

Flow: 

	GREET -> ASK FOR DIFFICULTY
		-> if ez -> 10 lives play game
		-> if hard -> 5 lives play gmae
			-> guess number
				-> if too high -> remove life, return too high -> add number to guessed / print guesses & try again
				-> if too low, same as above just return too low
					-> if win -> victory statement
					-> if loss -> loss statement
						-> end game and clear
		-> if bad answer end game and clear

