import deck

played = [0]

# Starts Simulation
#for z in range(1, 50):
#    # rolls
#    x = deck.cardRoll()
##    # put in array
#    played.append(x)
#    #Checks for dupes
#    if deck.cardCheck(played, x):
#        while deck.cardCheck(played, x):
#             x = deck.cardCheck(played, deck.cardRoll())

x = deck.cardRoll() + deck.cardRoll()
print(x)


def holder():
    quit = False
    while not quit:
        usr = (int(input("Enter 1 to play 2 to quit \n")))
        if usr == 1:
            for i in range(1, 3):
                x = deck.cardRoll()
                played.append(x)
                if deck.cardCheck(played, x):
                    while deck.cardCheck(played, x):
                        x = deck.cardCheck(played, deck.cardRoll())
                print(x)
            usr = (int(input("Enter 1 to hit 2 to stay \n")))
            if usr == 1:
                x = deck.cardRoll()
                played.append(x)
                if deck.cardCheck(played, x):
                    while deck.cardCheck(played, x):
                        x = deck.cardCheck(played, deck.cardRoll())
                print(x)


        else:
            quit = True