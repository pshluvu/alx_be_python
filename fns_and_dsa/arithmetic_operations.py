# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1: The first number.
        num2: The second number.
        operation (str): The operation to perform. Options: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the arithmetic operation, or an error message if invalid.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

