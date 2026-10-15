# Create an algorithm to determine whether a string is a palindrome or not
# Name: Reesa Zhou
# Date: October 14, 2026

palindrome = "racecar"
checker = 0
letterCount = 0

for i in palindrome:
    checker -= 1
    if i == palindrome[len(palindrome) + checker]:
        letterCount += 1

if letterCount == len(palindrome):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
