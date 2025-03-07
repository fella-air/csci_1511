# M. Overman, 3/6/2025
# lab 8, question 1

def find_UPC(entry):
    if len(entry) != 12:
        return False
    sum = 0

    for i in range(0, 11, 2):
        sum = sum + int(entry[i])

    sum *= 3

    for i in range(1, 10, 2):
        sum = sum + int(entry[i])
        
    m = sum % 10

    if m == 0:
        check_digit = 0
    else:
        check_digit = 10 - m

    if entry[-1] == str(check_digit):
        return True
    else:
        return False

result = find_UPC(str(input("Enter UPC: ")))

if result == True:
    print("VALID")
else:
    print("INVALID")