# Open a file and read its contents
# Name: Reesa Zhou
# Date: October 21, 2026

with open("names.txt", "r") as fileObject:
    contents = fileObject.read()
    print(contents)
    contentsList = contents.split("\n")
    print(F"Number of names: {len(contentsList)}")
