### --- PROJECT: TURTLE CROSSING CAPSTONE --- ###

Today's (day 23) is a capstone project. AKA a test? kinda. The objective is to use what
we have learnt about turtle to create a turtle crossing game. 

### --- PARAMETERS --- ###

Rules of turtle crossing

- The player starts at the bottom of the screen
- Cars randomly move across from right to left, despawning after they hit the end
- The player must navigate to the other side of the "road" without getting hit
- If they make it, the level and difficulty increases
- If not game over

### --- BREAKDOWN / NOTES --- ###

- Create the screen
    - This is going to be:
        - 600 x 600 px screen
        - White
        - Want tracer off for updating

- Create the turtle player
    - This is our turtle player, it will:
        - Start at -300, 0
        - be controllable with "w"
        - move north toward the finish line
            - We will use listeners and a move method to accomplish this

- Create the scoreboard
    - The scoreboard class will be nothing but:
        - A piece of text with "Level: X"
        - will tick up everytime the turtle reaches N, we can do the same with pong:
            - A score_point method, add_point method, called when it reaches the coords

- Detect collision with end
    - This is a simple if statement:
        if player.xcor() > 300:
            score_point()

- Create and move our Cars
    - This will be the hardest one:
        - We need randomized cars, starting at all sorts of positions on right hand side
        - We need to get them all to move
        - And finally when they hit the opposite side we need to make them despawn
            - For this I think a for loop, to create, randomly move them to starting positions
            and then move them will work / to also check if they are at edge 
            - we also want to create a way to kill any cars that leave the screen as 
            turtle objects don't get destroyed after leaving view. 

- Detect collision with cars:
    - Another simple if statement, as every car is a seperate object being created by a loop
    it stands to reason that we just need to create an if statement saying 
        - if player.distance(car) <50:
            game_over()

- Finally we want to make a game over class, in scoreboard. This will just be a piece of
text that says game over when we fail. 