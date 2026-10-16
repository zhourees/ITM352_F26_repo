def addition(num1, num2):
  while True:
    try:
      return num1 + num2
      break
    except ValueError:
      print("Invalid input. Try again.")
      continue

def subtraction(num1, num2):
  while True:
    try:
      return num1 - num2
      break
    except ValueError:
      print("Invalid input. Try again.")
      continue

def multiplication(num1, num2):
  while True:
    try:
      return round(num1 * num2, 2)
      break
    except ValueError:
      print("Invalid input. Try again.")
      continue

def division(num1, num2):
  while True:
    try:
      return round(num1 / num2, 2)
      break
    except ValueError:
      print("Invalid input. Try again.")
      continue

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
  print(addition(num1, num2))
elif operator == "-":
  print(subtraction(num1, num2))
elif operator == "*":
  print(multiplication(num1, num2))
else:
  print(division(num1, num2))
