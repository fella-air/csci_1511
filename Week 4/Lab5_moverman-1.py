# M. Overman, 2/16/2025
# lab 5, question 1

import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)

if (die1 + die2 == 2):
    term = "Snake Eyes"
elif (die1 + die2 == 3):
    term = "Ace caught a Deuce"
elif (die1 == 2 and die2 == 2):
    term = "Little Joe from Kokomo"
elif (die1 + die2 == 5):
    term = "Little Phoebe"
elif (die1 == 3 and die2 == 3):
    term = "Jimmy Hicks from the Sticks"
elif ((die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6)):
    term = "Six Ace"
elif (die1 == 4 and die2 == 4):
    term = "Eighter from Decatur"
elif (die1 + die2 == 9):
    term = "Nina from Pasadena"
elif (die1 == 5 and die2 == 5):
    term = "Puppy Paws"
elif ((die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6)):
    term = "Six Five no Jive"
elif (die1 + die2 == 12):
    term = "Boxcars"
else:
    term = ""

print(f"Die 1: {die1}, Die 2: {die2}")
print(f"Result: {die1 + die2} ({term})")