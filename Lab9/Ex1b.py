# Open a file using "with"
# Name: Reesa Zhou
# Date: October 21, 2026

with open("names.txt", "r") as fileObject:
    print(type(fileObject))

print("File is closed.", fileObject.closed)
