import random


class Account:

    def __init__(self, cName, cEmail, accountType, balance,pin = 0000, accountNum=random.randint(1000, 9999)):
        self.cName = cName
        self.cEmail = cEmail
        self.accountType = accountType
        self.balance = float(balance)
        if accountType == "student":
            self.balance += (balance * 0.5)
        self.accountNum = accountNum
        self.pin = pin

    def getName(self):
        return self.cName

    def getEmail(self):
        return self.cEmail

    def getAccountNumber(self):
        return self.accountNum

    def getAccountType(self):
        return self.accountType

    def getBalance(self):
        return self.balance

    def getPin(self):
        return self.pin

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setBalance(self, balance):
        self.balance = float(balance)
    def setPin (self, pin):
        self.pin = pin