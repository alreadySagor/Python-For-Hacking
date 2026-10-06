# Encapsulation

class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance # private attribute

    def deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def getbalance(self):
        return self.__balance

account = Bankaccount(1000)
account.deposite(500)
account.withdraw(2000)
print(f"Current balance is : {account.getbalance()}")

'''
self.balance --> Public attribute
self.__balance --> Private attribute
self._balance --> Protected attribute
'''