# Using else and Finally

try:
    num = int(input("Enter a number: "))
    print(f"You entered : {num}")
except ValueError:
    print("Error!!!\nEnter a valid number...")
else:
    print("The try block ran successfully.")
finally:
    print("End of error handling example.")