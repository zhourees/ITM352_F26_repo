def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return a / b


while True:
    print("\nSimple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit")

    try:
        user_input = input("Enter the first number: ")
        if user_input.lower() == 'q':
            break
        num1 = float(user_input)

        user_input = input("Enter the second number: ")
        if user_input.lower() == 'q':
            break
        num2 = float(user_input)

        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation selected.")
            continue

        print(f"Result: {result}")

    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

print("Goodbye!")
