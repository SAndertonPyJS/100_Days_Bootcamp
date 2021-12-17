Project 7 - Hangman

###--- PROJECT OBJECTIVES ---###

Today's project is a hangman game, the game must be able to follow the basic rules of hangman and work accordingly including

- Being able to allow letter inputs
- Cross checking that against the word
- Telling the user if they have guessed the letter before 
- Initiating strikes and steps towards the hangman
- Win conditions
- Fail conditions
- Ability to try again should the user want  

We will be taking two files and adding them to the main module. These will contain the art and words for importing

Flow chart of events:

START
    GENERATE RANDOM WORD

        GENERATE AS MANY BLANKS AS LETTERS

            ASK USER TO GUESS LETTERS

                IS IT CORRECT

                    >YES

                        REPLACE BLANKS

                            ALL BLANKS FILLED?

                                >YES

                                    GAME OVER

                                >NO

                                    GUESS AGAIN
                    >NO

                        LOSE A LIFE

                            RUN OUT OF LIVES?

                                >YES

                                    GAME OVER

                                >NO

                                    GUESS AGAIN
                
                    


