# Ex6c, but adds the input into the tuple by creating a new tuple
# Name: Reesa Zhou
# Date: October 2, 2026

data = ("hello", 10, "goodbye", 3, "goodnight", 5)

try:
    userInput = input("Add something to the tuple: ")
    data.append(userInput)
    print("Item was added!")
    print(data)
except AttributeError:
       newData = data + (userInput,)
       print("New tuple created to add item!")
       print(newData)
