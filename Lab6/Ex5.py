# Testing the use of assertions
# Name: Reesa Zhou
# Date: September 25, 2026

def cToF(celcius):
    assert celcius >= -273.15, "Temperature cannot be below absolute zero."
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

print(cToF(0))
print(cToF(100))
print(cToF(-300))
