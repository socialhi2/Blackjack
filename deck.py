import random as rnd

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def suitRoll():
    return rnd.randint(0, 3)

def valueRoll():
    return rnd.randint(1, 13)

def cardRoll():
    x = valueRoll()
    y = suitRoll()
    return x, suits[y]
def cardCheck(played_cards, new_card):
    return new_card in played_cards

def calculate_total(cards):
    total = 0
    for card in cards:
        value = card[0]
        if value > 10:
            total += 10
        else:
            total += value
    return total
