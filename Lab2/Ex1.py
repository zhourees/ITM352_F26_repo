# This program prompts the user to enter a number between 1 and 100, calculates the square of
# that number, and then prints both the entered number and its square.
# Name: Reesa Zhou
# Date: September 2, 2026

value_entered = input("Enter a number between 1 and 100: ");
value_as_integer = int(value_entered);

valueSquared = value_as_integer ** 2;

print("You entered:", value_as_integer);
print("The square of the entered number is:", valueSquared);

print(F"You entered: {value_as_integer}, and the square of that number is: {valueSquared}");
