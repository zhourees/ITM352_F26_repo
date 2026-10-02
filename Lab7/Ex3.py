# Check how many elements in a tuple are strings, and print the amount
# Name: Reesa Zhou
# Date: September 30, 2026

data = ("hello", 10, "goodbye", 3, "goodnight", 5)

stringCount = 0

for item in data:
    if type(item) == str:
        stringCount += 1;

print(F"There are {stringCount} strings in the tuple.")
