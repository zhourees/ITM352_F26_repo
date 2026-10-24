# Open a file and read the entire file using readlines()
# Name: Reesa Zhou
# Date: October 23, 2026

with open("names.txt", "r") as fileObject:
    names = fileObject.readlines()
    print(F"Number of names: {len(names)}")
    for name in names:
        print(name.strip())
