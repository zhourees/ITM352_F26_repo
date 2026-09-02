# Ask the user to enter a decimal number, calculate the square of that number, round it to two
# decimal places, and print it out.
# Name: Reesa Zhou
# Date: September 2, 2026

inputValue = input("Enter a floating point number: ");
floatValue = float(inputValue);
squaredValue = floatValue ** 2;
roundedValue = round(squaredValue, 2);

print("You entered:", floatValue);
print("The square of the number you entered is:", roundedValue);
