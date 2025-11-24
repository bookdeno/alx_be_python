def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.
    """

    if not isinstance(operation, str):
        return "Invalid operation"

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2

    if op == "subtract":
        return num1 - num2

    if op == "multiply":
        return num1 * num2

    if op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    return "Invalid operation"

