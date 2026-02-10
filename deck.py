import random as rnd

def suitRoll():
    return rnd.randint(0, 3)

def valueRoll():
    return rnd.randint(0, 12)

def cardRoll():
    x = valueRoll()
    y = suitRoll()
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    return x, suits[y]
def cardCheck(arr, card):
        # Checker for dupe
        for y in range(1, len(arr) - 1):
            if arr[y] == card:
                print("The card is equal")
        return False
