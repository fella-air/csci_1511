# M. Overman, 2/5/2025
# lab 4: deck of cards

import random

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["c", "h", "s", "d"]
full_deck = []

for s in suits:
    for v in values:
        full_deck.append(f"{v}{s}")

for x in range(int(input("Number of cards to draw "))):
    print(full_deck[random.randint(0, len(full_deck) - 1)])