# This program prompts the user to enter a temperature in Fahrenheit and then converts it to celcius
# Create the conversion as a function
# Name: Reesa Zhou
# Date: September 4, 2026

def F_to_C(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return round(celcius, 2);

fahrenheitInput = input("Please enter a temperature in fahrenheit: ");
fahrenheitFloat = float(fahrenheitInput);

celciusValue = F_to_C(fahrenheitFloat);

print("You entered:", fahrenheitFloat);
print("The temperature in celcius is:", round(celciusValue, 2));
