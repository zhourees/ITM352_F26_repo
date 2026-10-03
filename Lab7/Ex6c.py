# Ex6a with try-except statement
# Name: Reesa Zhou
# Date: October 2, 2026

data = ("hello", 10, "goodbye", 3, "goodnight", 5)

try:
    data.append(input("Add something to the tuple: "))
    print("Item was added!")
except AttributeError:
       print("Error! Attempt to add item failed.")
