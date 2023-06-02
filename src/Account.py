import random


class Account:

    def __init__(self, cName, cEmail, accountType, balance, accountNum=random.randint(1000, 9999)):
        self.cName = cName
        self.cEmail = cEmail
        self.accountType = accountType
        self.balance = balance
        if accountType == "student":
            self.balance += (balance * 0.5)
        self.accountNum = accountNum

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