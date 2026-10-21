# Open a file, read its contents, then append a new name at the end of the file
# Name: Reesa Zhou
# Date: October 21, 2026

with open("names.txt", "r") as fileObject:
    contentsList = fileObject.readlines()
    print(contentsList)

with open("names.txt", "a") as fileObject:
    print("Appending a new name to the file...")
    fileObject.write("\nJohn Doe")
