from Customer import Customer
from Account import Account
import random
import re

def run():
  customers = loadCustomers("customers.txt")
  accounts = loadAccounts("accounts.txt")
  activeAccount = login(accounts)
  checkBalance(activeAccount)
  transferFunds(activeAccount, accounts)


  '''
  
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

# this method prompts input from customer to create a new customer instance
def createCustomer():
  name = input("Please enter your name: ").capitalize()
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
def lowBalance(account):
    if int(account.getBalance()) < 100:
        print ("\nLow Balance \nAccounts balance is low, deposit money to avoid potential overdraft charges")
    print()
def login(accounts):
    #These variables are used to search through list of accounts and match name/email
    email = input("Please enter your email: ")
    name = input("Please enter your name: ")

    #carries the value of yes or no choice
    choice = ""
    flag = False
    foundAccount = None
    attempts = 0
    pin = 0

# Goes through all accounts and checks if name or email matches
    for account in accounts:
        if name.lower() == account.getName().lower() or email.lower() == account.getEmail().lower():
            choice = input ("Email: " + account.getEmail() + "\n Name: " + account.getName() + "\n is this your account (Y/N): ")
            if choice == 'Y' or choice == 'y':
                flag = True
                foundAccount = account


# if account exists in the list then prompts passcode
    if flag == True:
        while attempts < 3 and pin != foundAccount.getPin():
            pin = input("Please enter your 4 digit passcode: ")
            if (pin == foundAccount.getPin()) == False:
                     attempts +=1
                     print("Incorrect Pin you have " + str(3 - attempts) + " left" )
            else:
                lowBalance(foundAccount)
                return foundAccount



    print()

   #This method sends money from the logged in account to another account in the system
"""

   :param account: 
   :return: 
   """
def transferFunds(transferor, accounts):
   """
    fail cases:
    if the account doesnt have enough funds to transfer
    if the recipient account does not exist in the database
    if the sender doesnt confirm the transfer

    Sucess Conditions:
    The recepient account exiwsts, the active account has enough funds,
   """
   transferAmount = 0
   flag = False
   transferEmail = input("Please enter the email of the transfer account: ")
   tranferee = None
   option = ''
   for account in accounts:
       if transferEmail.lower() == account.getEmail().lower():
           transferee = account
           flag = True
           print ("\nAccount Found\n")
           break

   if flag == True:
        option = input(f"Name:{transferee.getName().capitalize()}\nEmail: {transferee.getEmail()}\n\nIs this the correct account (Y/N)")
        if option.lower() == 'y':
            transferAmount = input("Please enter the amount you would like to send:")
            transferAmount = int(transferAmount)
            if transferAmount >= transferor.getBalance():
               transferor.setBalance(transferor.getBalance() - transferAmount)
               transferee.setBalance(tranferee.getBalance() + transferAmount)

   if option.lower() != 'y':
        print("Thank You Please Come Again")

   else:
        print(f"Transfer Details:\nAmount Transfered:{transferAmount}\nTransfer Recepient: {transferee.getName().capitalize()}\n New Balance: {transferor.getBalance()}")
def checkBalance(account):
    print(f"Balance: ${account.getBalance()}")


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

        a1 = Account(customer.getName(), customer.getEmail(), customer.getOccupation(), balance,pin)

    return a1

# helper function that takes in an email address and returns true if the email address meets the required format
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
        accounts.append(Account(attributes[0],attributes[1],attributes[2], int(attributes[3]),attributes[4],attributes[5]))

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

    sourceFile = open("accounts.txt", 'w')

    for account in accounts:
        sourceFile.write(account.getName() + " " + account.getEmail() + " " + account.getAccountType() + " " +
        str(account.getBalance()) + " " + str(account.getPin()) + " " + str(account.getAccountNumber()) + '\n')

# This method takes in a list of customers then formats and saves the list into a file
def saveCustomers(customers):


    sourceFile = open("customers.txt", 'w')

    for customer in customers:
        sourceFile.write(customer.getName() + " " + str(customer.getAge()) + " " +
        str(customer.getEmail()) + " " + customer.getOccupation() + '\n')

run()