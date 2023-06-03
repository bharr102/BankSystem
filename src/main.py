from Customer import Customer
from Account import Account
import random
import re

def run():
  loadCustomers("customers.txt")
  loadAccounts("accounts.txt")
  accounts = loadAccounts()
  print(accounts[0].getName(),accounts[1].getName())
  customers = []
  '''
  c1 = createCustomer()
  c2 = createCustomer()
  customers.append(c1.getName())
  print(customers)
  x = re.findall("[0-9]{2}", str(c1.getAge()))
  print(x)
  account1 = createAccount(c1)
  a2 = createAccount(c2)
  accounts = [account1]
  accounts.append(a2)
 

'''
  saveAccounts(accounts)
  saveCustomers(customers)

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

# Checks balance whenever first logged in and prints out a message if balance is low *should work with the login function
def lowBalance():
    print()
def login(accounts):
    name = input("Please enter your name")
    email = input("Please enter your email")

    if name.lower() in accounts.getName().lower() and email.lower() in accounts.getEmail().lower():
        passwd = input (email + ":\nPlease enter your password")


    print()

   #This method sends a
def transferFunds():
    print()
def checkBalance():
    print()


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




#This function loads the program with bank  accounts from a specified file
def loadAccounts(infile):
    #infile = input("Please enter the  data files you would like to load:")
    sourceFile = open(infile, 'r')
    lines = sourceFile.readlines()
    accounts = []
    for line in lines:
        attributes = line.split()
        accounts.append(Account(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4]))

    return accounts
# This function loads data from a file and creates and returns a list of customers
def loadCustomers(infile):
    #infile = input("Please enter the  data files you would like to load:")
    sourceFile = open(infile, 'r')
    lines = sourceFile.readlines()
    customers = []
    for line in lines:
        attributes = line.split()
        customers.append(Customer(attributes[0],attributes[1],attributes[2],attributes[3]))

    return customers

# This method takes in a list of accounts, then formats and saves the list into a file
def saveAccounts(accounts):
    cusFileName = input("Please enter the file name you would like to save to: ")

    sourceFile = open(cusFileName, 'w')

    for account in accounts:
        sourceFile.write(account.getName() + " " + account.getEmail() + " " +
        str(account.getAccountNumber()) + " " + account.getAccountType() + " " + str(account.getBalance()) + '\n')

# This method takes in a list of customers then formats and saves the list into a file
def saveCustomers(customers):
    cusFileName = input("Please enter the file name you would like to save to: ")

    sourceFile = open(cusFileName, 'w')

    for customer in customers:
        sourceFile.write(customer.getName() + " " + customer.getAge() + " " +
        str(customer.getEmail()) + " " + customer.getOccupation() + '\n')

run()