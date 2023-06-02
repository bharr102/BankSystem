from Customer import Customer
from Account import Account
import random
import re

def run():
  customers = []
  c1 = createCustomer()
  customers.append(c1.getName())
  print(customers)
  x = re.findall("[0-9]{2}", str(c1.getAge()))
  print(x)
  account1 = createAccount(c1)
  accounts = [account1]




# this method prompts inpput from customer to create a new customer instance
def createCustomer():
  name = input("Please enter your name: ")
  age = input("Please enter your age: ")
  age = int(age)
  #Checking if email is a valid address
  email = input("Please enter your email: ")
  while (checkEmail(email) == False):
    print('Invalid email please try again')
    email = input("Please enter your email: ")
  occupation = input("Please enter your occupation: ")
  occupation = occupation.lower()
  c1 = Customer(name, age, email, occupation)
  return c1


# This method takes in a customer and creates an account based on the occupation and age of customer
def createAccount(customer):
    # to check if passcode meets the requirements
    flag = False
    passcodeSeq = "^[0-9]{4}$"
    # printing the romotion for students who make a new bank account
    print("\nWe add 50 % of initial balance deposit onto  new student account")

    balance = input("Please enter your first account deposit: ")
    balance = int(balance)

    while (flag == False):
        pin = input("Please enter a four digit passcode: ")
        validator = re.search(passcodeSeq, pin)
        if (validator == None):
            print("Invalid pin please try again \n")
            flag = False
        else:
            flag = True

        a1 = Account(customer.getName(), customer.getEmail(), customer.getOccupation(), balance)

    return a1

# this function takes in an email address and returns true if the email address meets the required format
def checkEmail(email):
    # creating regular experesion to define a correct email address
    emailSequence = "^[a-z0-9]+@[a-z]+\.(ca|com)$"

    # searching email provided to the email requirements
    x = re.search(emailSequence, email)
    valid = None

    if x == None:
        valid = False

    else:
        valid = True

    return valid


def login():
    print()


def loadFile():
    print()


def saveFile(accounts):
    cusFileName = input("Please enter the file name you would like to save to: ")

    sourceFile = open(cusFileName, 'w')

    for account in accounts:
        sourceFile.write(account.getName() + ";" + account.getEmail() + ";" + str(
            account.getAccountNumber()) + ";" + account.getAccountType() + ";" + account.getBalance())


run()