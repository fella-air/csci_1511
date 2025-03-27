# M. Overman, 3/26/2025
# lab 10, question 1

def main():
    try:
        filename = ("c:/Users/mfove/Documents/GitHub/csci_1511/Week 9/" + input("Enter file name: "))
    except FileNotFoundError:
        print("Invalid filename.")
    else:
        print("else")
        file = open(filename)
        frequency = wordFreq(file)
        printOut(frequency)
        file.close()

def wordFreq(fptr):
    freq = {}
    line = fptr.readline()
    punctChars = (".", ",", "!", "?", ":", ";", "'", "(", ")", "[", "]")
    while line:
        for c in punctChars:
            # removes all punctuation one type at a time
            line = line.replace(c, "")
        words = line.split()
        for word in words:
            tmp = word.lower()
            freq[tmp] = freq.get(tmp, 0) + 1
        line = fptr.readline()
    return freq

def printOut(data):
    for x in sorted(data.keys()):
        print(f"{x} :: {data[x]}") ## look at the formatting above
    return

main()