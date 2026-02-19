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

def play_blackjack():
    game_close = False

    # Main Menu Loop
    while not game_close:
        # Sets player to not be in game when booting program
        in_game = False
        usr = (int(input("Enter 1 to play 2 to quit \n")))
        # User entering 2 for quit
        if usr == 2:
            game_close = True
            continue
        # Main Game Loop
        if usr == 1:
            in_game = True
            played_cards = []
            player_cards = []
            dealer_cards = []
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

                print(f"Card: {card[0]} of {card[1]}")
            player_total = calculate_total(player_cards)
            print(f"Total: ", player_total)

            #Goes here if player does not start with 21
            while in_game:
                if player_total <= 21:
                    #Prints dealer's first card

                    # print("Utility 3: Reached if total < 21")
                    usr = int(input("Enter 1 to hit | Enter 2 to stay \n"))

                    if usr == 1:
                        # print("Utility 4: Reached if usr input is 1")
                        card = deck.cardRoll()
                        while deck.cardCheck(played_cards, card):
                            card = deck.cardRoll()
                        played_cards.append(card)
                        player_cards.append(card)
                        player_total = calculate_total(player_cards)
                        print(f"Card: {card[0]} of {card[1]}")
                        print(f"Total: {player_total}")

                    if usr == 2:
                        in_game = False
                        # print("Utility 5: Reached if usr input is 2")
                        end_message(player_total)

                if player_total > 21:
                    in_game = False
                    # print("Utility 6: Reached if total > 21")
                    end_message(player_total)


play_blackjack()