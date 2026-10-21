# Print numbers from 1 to n
# Print "Fizz" for multiples of 3, print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of 3 and 5
# Name: Reesa Zhou
# Date: October 14, 2026

for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
