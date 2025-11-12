# match_case_calculator.py
# A simple calculator using if-elif-else (works with Python 3.8)

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform calculation
if operation == '+':
    print(f"The result is {num1 + num2}.")
elif operation == '-':
    print(f"The result is {num1 - num2}.")
elif operation == '*':
    print(f"The result is {num1 * num2}.")
elif operation == '/':
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"The result is {num1 / num2}.")
else:
    print("Invalid operation selected.")

