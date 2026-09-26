# Create a list with different values and create outputs depending on certain conditions
# Name: Reesa Zhou
# Date: September 25, 2026

myList = ["one", "two", "three", "bread", "cheese", 1, 2, 3]

if(len(myList) < 5):
    print("There are less than five items on this list.")

elif(len(myList) >= 5 and len(myList) <= 10):
    print("There are between five and ten items on this list.")
else:
    print("There are more than ten items on this list.");

myListSmall = ["one", "two", "three"]
myListMedium = ["one", "two", "three", "bread", "cheese", 1, 2, 3]
myListLarge = ["one", "two", "three", "bread", "cheese", 1, 2, 3, 1, 2, 3]

if(len(myListSmall) < 5):
    print("There are less than five items on this list.")

if(len(myListMedium) >= 5 and len(myList) <= 10):
    print("There are between five and ten items on this list.")

if(len(myListLarge) > 10):
    print("There are more than ten items on this list.")
