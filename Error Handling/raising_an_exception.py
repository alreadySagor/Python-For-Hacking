# Raising an exception

def checkositive(number):
    if number < 0:
        raise ValueError("The number must be positive.")
    return number
try:
    print(checkositive(5))
except ValueError as e:
    print(f"Error {e}")