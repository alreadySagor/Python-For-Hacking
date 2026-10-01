# Handling multiple exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result : {result}")
except ValueError:
    print("Error!!!\nPlease enter a valid number...")
except ZeroDivisionError:
    print("Error!!!\nDivision by zero is not allowed...")