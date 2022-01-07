### --- OOP Coffee Machine --- ###

The project for today is revisiting the coffee machine and rebuilding it (to a degree)
in oop, as it's the first step into oop we are being provided with the classes and info in
the coffee_maker, menu and money_machine files and only have to write code in main.play


With that in mind:

### --- PARAMETERS --- ###

Program parameters can be found in the coffee machine parameters pdf

Flow: 

	Greet user -> ask which coffee they want
        -> once selected, check the coffee resources for sufficient amount
            -> if sufficient
                -> ask for payment
                    -> if enough coins 
                        -> process transaction
                        -> make coffee
                    -> else
                        -> refund coins 
                        -> next customer
            -> else
                -> let user know to contact staff
        -> if not valid choice let user know -> next customer

    -> Include functionality for off and report