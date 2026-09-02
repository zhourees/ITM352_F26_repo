# Ask the user to enter their birth year, calculate their age based on the current year and print it out.
# Name: Reesa Zhou
# Date: September 2, 2026

birthYear = input("Enter your birth year: ");
currentYear = 2026;
age = currentYear - int(birthYear);

print("You entered:", birthYear);
print("Your age is: " + str(age));
