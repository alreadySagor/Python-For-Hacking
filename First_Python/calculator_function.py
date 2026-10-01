# Calculator Function

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divde(a, b):
    if b != 0:
        return a / b
    else:
        print("Error!!! Divison by Zero")

# User Interface:
print("Welcome")
print("Choose an Operation : +, -, *, /")

operation = input("Enter the Operation: ")
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))
if operation == '+':
    print(f"Result  (additon): {add(num1, num2)}")
elif operation == '-':
    print(f"Result  (subtraction): {subtract(num1, num2)}")
elif operation == '*':
    print(f"Result  (multiplication): {multiply(num1, num2)}")
elif operation == '/':
    print(f"Result  (Division): {divde(num1, num2)}")
else:
    print("Invalid Operation")