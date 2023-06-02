class Customer:
    def __init__(self, name, age, email, occupation):
        self.name = name
        self.age = age
        self.email = email
        self.occupation = occupation
        # gets and returns the name of the Customer

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getEmail(self):
        return self.email

    def getOccupation(self):
        return self.occupation

    def setName(self, name):
        self.name = name

