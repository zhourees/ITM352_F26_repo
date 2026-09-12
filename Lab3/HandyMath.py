# Includes three math functions that calculates exponents, maximum, and minimum
# Name: Reesa Zhou
# Date: September 11, 2026

def midpoint(num1, num2):
    return ((float(num1) + float(num2)) / 2);

def squareroot(n):
    return (float(n)) ** 0.5;

def exponent(base, exponent):
    return (float(base)) ** (float(exponent));

def max(num1, num2):
    if(num1 > num2):
        return float(num1);
    if(num2 > num1):
        return float(num2);

def min(num1, num2):
    if(num1 < num2):
        return float(num1);
    if(num2 < num1):
        return float(num2);
