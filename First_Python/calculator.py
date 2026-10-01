# this is a calculator project

print("Simple calculator")
num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))

print(" Operations : +, -, *, /")
operation = input("Enter the operation : ")

if operation == '+':
    print("result is :", num1 + num2)
elif operation == '-':
    print("result is :", num1 - num2)
elif operation == '*':
    print("result is :", num1 * num2)
elif operation == '/':
    print("result is :", num1 / num2)
else:
    print("Try again  by using on of these operators (+, -, *, /)")