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