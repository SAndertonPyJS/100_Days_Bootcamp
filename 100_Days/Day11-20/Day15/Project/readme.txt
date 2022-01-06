### --- COFFEE MACHINE --- ###

Todays project is the coffee machine we have to create a piece of code that behaves like such

### --- REQ --- ###

1/ Print report -> resources left, cash in possession

2/ Check resources sufficient 

3/ process coins

4/ Check transaction successful

5/ Make coffee -> Deduct resources / add money


### --- FLOW --- ###

The program should (and this can double as project directives to prevent retyping)

Greet the user
    -> Ask the user to choose from the drinks menu
        -> when a user chooses a valid option (give user info if option invalid)
            -> ask for cash (machine is coin operated 1, 5, 10, 25c)
                -> if correct 
                    -> process coins
                    -> check coffee resources
                        -> if enough
                            -> make coffee
                        -> if not enough
                            -> return info about availability and ask user to ask for a refill

                -> if incorrect
                    -> refund change if not enough
                    -> if too much return change -> proceed to process coins/ check resources