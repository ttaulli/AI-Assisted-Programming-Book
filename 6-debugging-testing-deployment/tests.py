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

# Test-Driven Development (TDD)
# Tests are written before the actual code
# Write test + make it fail + write code to pass it + refactor 
# Prompt:  I want to use the test-drive development process for building a Python function that calculate whether a number is prime.  So write a failing test.
# Prompt:  Write code to make the test pass with minimal implementation.
# Prompt:  Refactor



breakpoints = {
    'xs': '320',
    'sm': '576',
    'md': '768',
    'lg': '992',
    'xl': '1200',
}