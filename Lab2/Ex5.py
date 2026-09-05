# This program prompts the user to enter a string and then calculates
# and displays the length of that string
# Name: Reesa Zhou
# Date: September 4, 2026

userString = input("Please enter a password: ");
stringLength = len(userString);

print("You entered:", userString);
print("The length of the password you entered is:", stringLength);

if(stringLength <= 10):
    print("This is an ineffective string.");

if(stringLength >= 10):
    print("This is an effective string.");