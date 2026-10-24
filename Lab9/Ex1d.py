# Open a file and read it by line
# Name: Reesa Zhou
# Date: October 23, 2026

with open("names.txt", "r") as fileObject:
  while (line := fileObject.readline()):
    print(line.strip())
