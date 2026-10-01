# Print odd numbers between 1 - 50 using list comprehension
# Name: Reesa Zhou
# Date: September 30, 2026

oddNum = [2 * num + 1 for num in range(0, 50) if 2 * num + 1 < 50]
print(oddNum)
