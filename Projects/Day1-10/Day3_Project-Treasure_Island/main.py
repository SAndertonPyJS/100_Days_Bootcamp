#we must create a basic treasure island game, the idea is to creat a 4 step multiple choice system
#where we pick between two options, sometimes three, and have to obtain a treasure at the end

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#first choice
direction = input("You arrive on an island, there are two paths, one leading into a thick jungle, the other a path up a mountain, which do you choose? left or right?: ").lower()

false_direction = "You head deep into the jungle, cutting through the vines as you go, eventually lost, struggling to make bearings you realize you cannot escape, the forest claims another"
true_direction = "You head up the mountain path, finding that it's tough but fair, eventually you come to a fork in the road one leading up the other leading downwards"

#now we want to setup conditionals that we will use throughout the code: 

if direction == 'left':
    print(true_direction)

#second choice
#we want the code to only continue if path stays true

    fork = input("You contemplate which path to take, up seems safer, where down leads into the jungle, where do you go? up or down?: ").lower()

    true_fork = "You descend the mountain path, heading down into the forest, after what seems like hours of ducking through the undergrowth you encounter a lake with an island in the middle"
    false_fork = "You head up the mountain, confident, as the mountain gets harder to traverse, you end up slipping and fall, you worriedly think about what would have happened had you gone down as you fall to your demise"

    if fork == 'down':
        print(true_fork)

            #third choice

        lake = input("You see a boat at the edge of the lake and think about crossing, as you contemplate you hear something behind you panicking you decide, do you cross or run?: ").lower()

        true_lake = "You jump in the boat and begin to cross the lake, just as a massive bear comes hurtling out of the woods, close one you think as you float away, the boat eventually reaches the island"
        false_lake = "You decide to run for it as a huge bear runs into the clearing, seeing you running it begins to chase you down, this is where your story ends, chased down by a bear. Maybe crossing the lake would have been better"

        if lake == "cross":
            print(true_lake)
            
            #final choice
            door = input("You find a house with three identical doors, all similar in every way except color, a message above choose correctly and Treasure there be, which do you choose red, yellow, blue?: ").lower()

            true_door = "You confidently swing open the red door, sure that you are correct, stepping inside you find troves of treasure piling high, as far as the eye can see, you're rich!!!"
            false_door_1 = "You open the blue door and step inside, the door slams shut behind you,in the pitch black you see a single set of glowing red eyes... they slowly start approaching you"
            false_door_2 = "You open the yellow door, looking inside to see what seems like a bottomless pit, just as you are about to back away the bear from before has run up behind startling you, as you stumble and fall you curse yourself remembering bears can in fact, swim."

            if door == 'red':
                print(true_door)
            elif door == 'blue':
                print(false_door_1)
            elif door == 'yellow':
                print(false_door_2)

            #third choice fails
        if lake == 'run':
            print(false_lake)

    #second choice fails
    if fork == 'up':
        print(false_fork)

#first choice fails

elif direction == 'right':
    print(false_direction)


    
