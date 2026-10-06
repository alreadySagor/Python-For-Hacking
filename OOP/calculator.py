# using more methods

class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, number):
        self.value += number
        return self.value
    def subtract(self, number):
        self.value -= number
        return self.value

calc = Calculator(10)
print(f"Initial Value : {calc.value}")
print(f"After adding 5 : {calc.add(5)}")
print(f"After subtracting 4 : {calc.subtract(4)}")