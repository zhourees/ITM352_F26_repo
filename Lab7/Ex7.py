# Iterate through 1 - 10, printing the numbers (except 5) and breaking at 8
# Name: Reesa Zhou
# Date: October 2, 2026

for number in range(1, 11):
    if number >= 8:
        print("Stopping.")
        break
    if number != 5:
        print(number)
        continue
