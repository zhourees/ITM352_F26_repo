# Create an algorithm to search if an user input exists in an array
# Name: Reesa Zhou
# Date: October 14, 2026

searchMe  = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

userInput = int(input("Please enter an integer: "))
exists = False

for n in searchMe:
    if userInput == n:
        print(F"{userInput} is in the array of numbers.")
        exists = True

if exists == False:
    print(F"{userInput} does not exist in this array.")
