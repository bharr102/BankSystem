
class Transcript:
    def __init__(self, date, time ,amount,endingBalance,transType,email):
        self.date = date
        self.time = time
        self.amount = float(amount)
        self.endingBalance = float(endingBalance)
        self.transType = transType
        self.email = email

    def printReport(self):
        print("{} {} ${:.2f}\nEnding Balance: ${:.2f}\n ".format(self.date, self.transType.upper(),self.amount,self.endingBalance))


    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def getAmount(self):
        return self.amount
    def getEndingBalance(self):
        return self.endingBalance
    def getTransType(self):
        return self.transType
    def getEmail(self):
        return self.email