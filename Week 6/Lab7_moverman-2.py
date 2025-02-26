# M. Overman, 2/26/2025
# lab 7, question 2

import random

answer = 0
correctNum = random.randint(1,100)

answer = int(input("What is the number? (1 to 100)"))
guesses = 1

while answer != correctNum:
    guesses += 1
    answer = int(input("What is the number? (1 to 100)"))

print("Congratulations! You won in", guesses, "guesses!")