# Using two inputted integers, this program calculates midpoint, square root, raises one number to the exponent of the other,
# and finds the maximum and minimum
# Name: Reesa Zhou
# Date: September 11, 2026

import HandyMath

integerOne = input("Enter the first digit: ");
integerTwo = input("Enter the second digit ");

print(f"You entered the digits {integerOne} and {integerTwo}.");

print(f"The midpoint of these digits is {HandyMath.midpoint(integerOne, integerTwo)}.");

print(f"The square root of {integerOne} is {HandyMath.squareroot(integerOne)}.");

print(f"{integerOne} raised to the power of {integerTwo} is {HandyMath.exponent(integerOne, integerTwo)}.");

print(f"The max of these two digits is {HandyMath.max(integerOne, integerTwo)}.");

print(f"The min of these two digits is {HandyMath.min(integerOne, integerTwo)}.");
