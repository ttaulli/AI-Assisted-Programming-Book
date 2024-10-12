# Unit tests
# Check the functionality of individua units of code, such as functions or methods, in isolation
# Prompt: /tests 


# The factorial of a non-negative integer n is the product of 
# all positive integers less than or equal to


def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



# Prompt:  Are there any other edge cases that should be tested?

# Prompt:  Create validation for the n argument