import pandas as pd
import numpy as np

class BankAccount: 
    def __init__(self, name, balance = 0.0):
        self.log ("Account created!")
        self.name = name
        self.balance = balance

    def getBalance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.log("Money deposited.")

    def withdraw(self, amount):
        self.balance -= amount
        self.log("Money withdrawn.")

    def log(self, message):
        myLog = open("Log.txt", "a")
        print(message, file = myLog)
        myLog.close()
    
myAccount = BankAccount("Brandon Trent", 25.00)
print(myAccount.getBalance())

myAccount.deposit(10.00)
print(myAccount.getBalance())

myAccount.withdraw(5.25)
print(myAccount.getBalance())

wifeAccount = BankAccount("wife", 55.00)
print(wifeAccount.getBalance())