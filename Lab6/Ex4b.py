# Define function to check if inputted year is leap year
# Name: Reesa Zhou
# Date: September 25, 2026

def isLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year."
    else:
        return "is not a leap year."

yearInput = int(input("Enter a year: "))
print(isLeapYear(yearInput))
