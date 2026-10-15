# Give $0.47 of change in quarters, dimes, nickels, and pennies
# Name: Reesa Zhou
# Date: October 14, 2026

import math

owed = 0.57
givenAmount = 1
change = givenAmount - owed
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if change / 0.25 > 0:
    quarters = 0.25 * math.floor(change / 0.25)
    change -= quarters

if change / 0.10 > 0:
    dimes = 0.10 * math.floor(change / 0.10)
    change -= dimes

if change / 0.05 > 0:
    nickels = 0.05 * math.floor(change / 0.05)
    change -= nickels

pennies += change

print(F"The change amount is ${round(quarters, 2)} in quarters, ${round(dimes, 2)} in dimes, ${round(nickels, 2)} in nickels, and ${round(pennies, 2)}\
 in pennies.")
