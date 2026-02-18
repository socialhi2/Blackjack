import deck
from deck import calculate_total

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

#x1, y1 = deck.cardRoll()
#x2, y2 = deck.cardRoll()
#print("Your cards: ", x1, y1, " and ", x2, y2, "Your total is: ", x1 + x2)

def end_message(wn):
    if wn == 1:
        print("You have won!")
    if wn == 0:
        print("You lost!")

def play_blackjack():
    cc = 0
    game_close = False
    # Main Menu Loop
    while not game_close:
        usr = (int(input("Enter 1 to play 2 to quit \n")))
        # User entering 2 for quit
        if usr == 2:
            game_close = True
            continue
        # Main Game Loop
        if usr == 1:
            played_cards = []
            for _ in range(2):
                card = deck.cardRoll()
                while deck.cardCheck(played_cards, card):
                    card = deck.cardRoll()
                played_cards.append(card)
                print(f"Card: {card[0]} of {card[1]}")
            total = calculate_total(played_cards)
            print(f"Total: ", total)

            #Goes here if player does not start with 21
            if total < 21:
                usr = int(input("Enter 1 to hit | Enter 2 to stay \n"))
                if usr == 1:
                    card = deck.cardRoll()
                    while deck.cardCheck(played_cards, card):
                        card = deck.cardRoll()
                    played_cards.append(card)
                    total = calculate_total(played_cards)
                    print(f"Card: {card[0]} of {card[1]}")
                    print(f"Total: {total}")


play_blackjack()