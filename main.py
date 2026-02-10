import random as rnd
suitRoll = rnd.randint(1, 4)
cardRoll = rnd.randint(1, 13)
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

print("Your card is: ", cardRoll, " of ", suits[suitRoll])
