# Create a list of odd numbers between 1 - 50 using a for-statement
# Name: Reesa Zhou
# Date: September 30, 2026

oddNum = []

for num in range(1,51):
    if num % 2 != 0:
        oddNum.append(num);

print(oddNum)
