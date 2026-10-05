class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayinfo(self):
        print(f"My name is {self.name} and i'm {self.age} years old.")

Person1 = Person('Dr. Doom', 60)
Person1.displayinfo()