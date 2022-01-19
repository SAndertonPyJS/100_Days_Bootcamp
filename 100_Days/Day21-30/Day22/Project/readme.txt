### --- PROJECT: PONG GAME --- ###

Today's (day 22) project is to build the pong game in OOP, it will in all effect function
exactly like the pong game from arcade machines. As this is a larger project it's going to be split
into 7 major steps to tackle:

### --- PARAMETERS --- ###

Rules of Pong

Two paddles are controlled at opposite ends of the arena
A ball bounces between the arena and the paddles
The objective is to hit the ball with the paddle back and forth until one player scores (The ball goes past the paddle to the goal)
The ball is then reset, score is added and we begin again, first to 5 wins

### --- BREAKDOWN --- ###

- Create the screen

- Create and move a paddle
    - This will be an object, we will want to use event listeners to make it move and it should only be able to move up or down

- Create the second paddle
    - Same as before we create and move the second, want to bind it to different keys so it's controlled independently

- Detect collision with a wall and bounce
    - This will be the hardest one as we need to figure out how to get it to bounce
        - The primary idea I have for this is when it detects a collision it inverts it's movement but we will need to check this out

- Detect paddle collision
    - WE will setup a statement for the objects stating if they are within 15 px of each other (and ball is not at goal) it counts as a hit

- Detect when the paddle misses
    - This will be the same collision detection as snake, we will want to detect if it comes within range of the goal, while a paddle
    object is considered out of range

- Keep score
    - This is an easy one, similar to the snake game we can set two score objects, if the ball reaches the objects
    goal we can trigger the reset. Same as before but with two instead of one.