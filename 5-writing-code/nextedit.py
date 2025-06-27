# Rename pizza to pizzaType.

pizza = 'Pepperoni'
print(pizza)


# Add parameters

def greet(first_name):
    print("Hello, " + first_name + "!")

# Changing class/method/function names
# change class to 3DPoint

import math

class Point:
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y

    def get_distance(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
# Refractoring
# Change greet to farewell

# Function with Default Parameters

def multiply(a: float, b: float = 1) -> float:
    return a * b

# Function with Optional Parameters; use farewell
def greet(name: str, greeting: str = None) -> str:
    return f"{greeting or 'Hello'}, {name}!"

# Fibonacci function
def fib(n: int) -> int:
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

