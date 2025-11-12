# match_case_calculator.py
# ALX-compatible simple calculator
# Uses match-case if available (Python 3.10+), otherwise falls back to if/elif/else

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

try:
    # Attempt Python 3.10+ match-case
    exec("""
match operation:
    case '+':
        print(f"The result is {num1 + num2}.")
    case '-':
        print(f"The result is {num1 - num2}.")
    case '*':
        print(f"The result is {num1 * num2}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("Invalid operation selected.")
""")
except SyntaxError:
    # Fallback for Python <3.10
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

