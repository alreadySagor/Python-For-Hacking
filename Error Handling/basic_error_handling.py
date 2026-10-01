# Basic Error Handling

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error!!!\nYou must enter a valid number...")