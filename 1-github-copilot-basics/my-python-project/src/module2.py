# module2.py

def function_in_module2():
    print("This is a function in module2")

def function_in_module2_calling_module1():
    from module1 import function_in_module1
    function_in_module1()