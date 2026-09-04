# This program prompts the user to enter a weight in pounds and then calculates and displayes the
# equivalent in kilograms
# Name: Reesa Zhou
# Date: September 4, 2026

print(F"Your weight in kilograms is: {int(input("Please enter your weight in pounds: "))*0.453592}.");

poundsToKg = 0.453592;
weightInPounds = input("Please enter your weight in pounds: ");
weightInPoundsFloat = float(weightInPounds);
weightInKilos = (weightInPoundsFloat * poundsToKg);

print("You entered:", weightInPounds);
print("Your weight in kilograms is:", weightInKilos);
