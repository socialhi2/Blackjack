import deck
from deck import calculate_total


# Starts Simulation (THIS IS NOT UPDATED TO RECENT CODE)
#played = [0]
#for z in range(1, 50):
#    # rolls
#    x = deck.cardRoll()
##    # put in array
#    played.append(x)
#    #Checks for dupes
#    if deck.cardCheck(played, x):
#        while deck.cardCheck(played, x):
#             x = deck.cardCheck(played, deck.cardRoll())
#x1, y1 = deck.cardRoll()
#x2, y2 = deck.cardRoll()
#print("Your cards: ", x1, y1, " and ", x2, y2, "Your total is: ", x1 + x2)


def dealer():
    # This is for the dealer
    print("This is a holder")


def end_message(total):
    # print("Utility 1: End message reached")
    if total < 21:
        # print("Utility 7: Win message reached")
        print("You have won!")
    if total > 21:
        # print("Utility 2: Loss message reached")
        print("You lost!")

# Main code for the game
def play_blackjack():
    # game_close set to false when game is started
    game_close = False

    # Main Menu Loop
    while not game_close:
        # Sets player to not be in game when booting program
        in_game = False

        # User input to ask if player will play or stop. It will always loop back here.
        usr = (int(input("Enter 1 to play 2 to quit \n")))


        # User entering 2 to quit game
        if usr == 2:
            game_close = True
            continue


        # Main Game Loop
        if usr == 1:
            # Sets player to be in game
            in_game = True
            played_cards = []
            player_cards = []
            dealer_cards = []
            # Dealer and Player gets 2 cards each
            for _ in range(2):
                # Dealer gets first card
                card = deck.cardRoll()
                while deck.cardCheck(played_cards, card):
                    card = deck.cardRoll()
                # Appends card to the total and dealer
                played_cards.append(card)
                dealer_cards.append(card)


                # Player goes second
                card = deck.cardRoll()
                while deck.cardCheck(played_cards, card):
                    card = deck.cardRoll()
                played_cards.append(card)
                player_cards.append(card)

                #Prints player's card so player can see
                print(f"Card: {card[0]} of {card[1]}")
            # Calculates total using the player_cards array
            player_total = calculate_total(player_cards)
            # Prints player's total
            print(f"Total: ", player_total)

            #Goes here if player does not start with 21
            while in_game:
                if player_total <= 21:
                    #Prints dealer's first card (WIP)

                    # print("Utility 3: Reached if total < 21")
                    # User input to get a card or to stay
                    usr = int(input("Enter 1 to hit | Enter 2 to stay \n"))

                    # Player gets delt a card
                    if usr == 1:
                        # print("Utility 4: Reached if usr input is 1")
                        # Player gets a card
                        card = deck.cardRoll()
                        # Checks the card with what has been played
                        while deck.cardCheck(played_cards, card):
                            card = deck.cardRoll()
                        # Appends the card to the total played and player's array
                        played_cards.append(card)
                        player_cards.append(card)
                        # Recalculates player's total of cards
                        player_total = calculate_total(player_cards)
                        # Prints the new card and player's total
                        print(f"Card: {card[0]} of {card[1]}")
                        print(f"Total: {player_total}")
                    # User chooses to stay
                    if usr == 2:
                        in_game = False
                        # print("Utility 5: Reached if usr input is 2")
                        # Gets sent to end message to calculate who wins
                        end_message(player_total)

                # Player loses
                if player_total > 21:
                    in_game = False
                    # print("Utility 6: Reached if total > 21")
                    # Gets sent to end message to calculate who wins
                    end_message(player_total)

# Calling the function for people to play
play_blackjack()