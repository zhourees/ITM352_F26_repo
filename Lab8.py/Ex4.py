# Find the GCD (greatest common divisor) of two chosen numbers
# Name: Reesa Zhou
# Date: October 14, 2026

num1 = 27
num2 = 99
gcd = 0

for n in range(1, num1 + 1):
    if num1 % n == 0 and num2 % n == 0:
        if n > gcd:
            gcd = 0
            gcd += n

print(F"The GCD of {num1} and {num2} is {gcd}.")
