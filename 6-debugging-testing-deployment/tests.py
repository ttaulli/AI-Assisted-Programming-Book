# Unit tests
# Check the functionality of individua units of code, such as functions or methods, in isolation

def add(a, b):
    return a + b


# Integration testing
# When units or components are tests as a group
# Goal is to verfiy that the interactions between the units are working as expected

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def add_and_multiply(a, b, c):
    return multiply(add(a, b), c)

# Performance testing
# Focus on speed, responsiveness, and stability of the system under a particular workload

import time

def slow_function():
    time.sleep(2)
    return True