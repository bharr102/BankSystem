
class Transcript:
    def __init__(self, date, time ,amount,endingBalance,transType,email):
        self.date = date
        self.time = time
        self.amount = amount
        self.endingBalance = endingBalance
        self.transType = transType
        self.email = email

    def printReport(self):
        print("Date: {} Time: {} Amount: {}\nEnding Balance: {} ".format(self.date, self.time,self.amount,self.endingBalance))