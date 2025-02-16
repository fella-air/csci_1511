# M. Overman, 1/23/2025
# lab 2, question 3

original = input("Enter message to be reversed: ")

for i in range(len(original), 0, -1):
    print(original[i - 1], end="")