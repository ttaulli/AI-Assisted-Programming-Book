def calculate(operation, a, b):
    """
    Perform a calculation between two numbers.
    
    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
        a: First number
        b: Second number
        
    Returns:
        float or int: Result of the calculation
        
    Raises:
        TypeError: If a or b are not numeric
        ValueError: If operation is invalid or if dividing by zero
    """
    # Check if inputs are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numeric values")
    
    # Perform requested operation
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Invalid operation: {operation}. Valid operations are: add, subtract, multiply, divide")

# Example usage
if __name__ == "__main__":
    print("Calculator Program")
    print("-----------------")
    
    try:
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        result = calculate(operation, a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")