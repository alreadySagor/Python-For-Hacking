# Define Simple Function
def greet():
    print("Hello, World")

# Functions with Parameters
def greet_user(name):
    print(f"Hello , {name}!")

greet_user("Sagor")
greet_user("Salim")
greet_user("Dola")

def add_numbers(a, b):
    return a + b
Outcome = add_numbers(10, 20)
print(Outcome)
print(f"{add_numbers(100, 20)}")

# Default Parameters
# (If the user doesn't provide any parameter, it will be "Guest" by default)
def greetuser(name = 'Guest'):
    print(f"hello, {name}")

greetuser()
greetuser('Zaid')

# Modules

import math
print('square root of 16', math.sqrt(16))
print('Value of pi', math.pi)