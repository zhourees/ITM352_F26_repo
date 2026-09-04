# This program prompts the user to enter a temperature in Fahrenheit and then converts it to celcius
# Name: Reesa Zhou
# Date: September 4, 2026

fahrenheitInput = input("Please enter a temperature in fahrenheit: ");
fahrenheitFloat = float(fahrenheitInput);

celciusValue = (fahrenheitFloat - 32) * 5/9;

print("You entered:", fahrenheitFloat);
print("The temperature in celcius is:", round(celciusValue, 2));
