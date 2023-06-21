import time
from datetime import date
from Customer import Customer
from Account import Account
from Transcript import Transcript
import random
import re

def run():
  customers = loadCustomers("customers.txt")
  accounts = loadAccounts("accounts.txt")
  transcripts = loadTranscripts("transcriptions.txt")
  activeAccount = login(accounts)

  ## checkBalance(activeAccount)
  ## transferFunds(activeAccount, accounts)



  if activeAccount != None:
    option = input(
          "Select an option \n(1) Check Balance\n(2) Deposit\n(3) Withdraw\n(4) Transfer\n(5) Show Transactions\n(0) Exit\n")
    option = int(option)
    while option != 0:
      if option == 1:
          checkBalance(activeAccount)
      elif option == 2:
          depReceipt = deposit(activeAccount)
          transcripts.append(depReceipt)
      elif option == 3:
          withReciept = withdraw(activeAccount)
          transcripts.append(withReciept)
      elif option == 4:
         reciept = transferFunds(activeAccount, accounts)
         transcripts.append(reciept)

      elif option == 5:
        for reciept in transcripts:
            if reciept != None:
                if reciept.email == activeAccount.getEmail():
                    reciept.printReport()

      elif option == 0:
          print("Thank You Please Come Again!")
          break
      else:
          print ("Invalid Choice")

      option = input(
          "Select an options \n(1) Check Balance\n(2) Deposit Money\n(3) Withdraw Money\n(4)Transfer Money\n(5)Show Transactions\n(0) to exit\n")
      option = int(option)
  else:
      print ("Account Not Found.\nPlease try again.")
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
  saveTranscripts(transcripts)

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
    if float(account.getBalance()) < 100:
        print ("\nWARNING:Low Balance")
    print()
def login(accounts):
    #These variables are used to search through list of accounts and match name/email
    flag = False
    email = input("Please enter your email: ")
    while (flag == False):
        if checkEmail(email) == True:
            flag = True
        else:
            email = input("Invalid email, Please enter your email: ")
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
            choice = input ("Email: " + account.getEmail() + "\nName: " + account.getName().capitalize() + "\nis this your account (Y/N): ")
            if choice.lower() == 'y':
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
   transferee = None
   option = ''
   for account in accounts:
       if transferEmail.lower() == account.getEmail().lower():
           transferee = account
           flag = True
           print ("\nACCOUNT FOUND")
           break

   if flag == True:
        option = input(f"Name:{transferee.getName().capitalize()}\nEmail: {transferee.getEmail()}\n\nIs this the correct account (Y/N)")
        if option.lower() == 'y':
            transferAmount = input("Please enter the amount you would like to send:")
            transferAmount = float(transferAmount)
            if transferAmount <= transferor.getBalance():
               todaysDate = date.today()
               timeNow = time.localtime()
               timeNow = time.strftime("%H:%M:%S",timeNow)

               transferor.setBalance(transferor.getBalance() - transferAmount)
               transferee.setBalance(transferee.getBalance() + transferAmount)

               receipt = Transcript(todaysDate,timeNow,transferAmount,transferor.getBalance(), "Transfer", transferor.getEmail())
               return receipt
            else:
                print("Insufficient Funds")

   if option.lower() != 'y':
        print("Thank You Please Come Again")

   else:
        print(f"Transfer Details:\nAmount Transfered:${transferAmount}\nTransfer Recepient: {transferee.getName().capitalize()}\nNew Balance: ${transferor.getBalance()}")
def checkBalance(account):
    print("Account Balance: ${:.2f}\n".format(account.getBalance()))

## This method removes money from the logged in accounts balance
def deposit(account):
    pmt = input("Please enter Deposit Amount: ")
    pmt = float(pmt)
    print("\nDeposit Amount ${:.2f}\nY/N".format(pmt))
    choice = input ()
    if choice.lower() == 'y':
        account.setBalance(account.getBalance() + pmt)
        todaysDate = date.today()

        timeNow = time.localtime()
        timeNow = time.strftime("%H:%M:%S", timeNow)

        receipt = Transcript(todaysDate, timeNow, pmt, account.getBalance(), "Deposit",
                             account.getEmail())
        return receipt


## This method adds money from the logged in accounts balance
def withdraw(account):
    pmt = input("Please Enter the Withdrawal Amount: ")
    pmt = float(pmt)

    if account.getBalance() < pmt:
        print("Insufficient Funds.\n")
    else:
        print("\nWithdraw Amount ${:.2f}\nY/N".format(pmt))
        choice = input()
        if choice.lower() == 'y':
            account.setBalance(account.getBalance() - pmt)

            todaysDate = date.today()

            timeNow = time.localtime()
            timeNow = time.strftime("%H:%M:%S", timeNow)

            receipt = Transcript(todaysDate, timeNow, pmt - pmt*2, account.getBalance(), "Withdraw",
                             account.getEmail())
            return receipt
# This method takes in a customer and creates an account based on the occupation and age of customer
def createAccount(customer):
    # to check if passcode meets the requirements
    flag = False
    passcodeSeq = "^[0-9]{4}$"
    # printing the romotion for students who make a new bank account
    print("\nWe add 50 % of initial balance deposit onto  new student account")

    balance = input("Please enter your first account deposit: ")
    balance = float(balance)

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
    emailSequence = "^[a-zA-Z0-9]+@[a-zA-Z]+\.(ca|CA|COM|com)$"

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

    sourceFile = open(infile, 'r')
    lines = sourceFile.readlines()
    accounts = []
    for line in lines:
        attributes = line.split()
        accounts.append(Account(attributes[0],attributes[1],attributes[2], float(attributes[3]),attributes[4],attributes[5]))

    return accounts
# This function loads data from a file and creates and returns a list of customers
def loadCustomers(infile):

    sourceFile = open(infile, 'r')
    lines = sourceFile.readlines()
    customers = []
    for line in lines:
        attributes = line.split()
        customers.append(Customer(attributes[0],attributes[1],attributes[2],attributes[3]))

    return customers

def loadTranscripts(infile):

    sourceFile = open(infile, 'r')
    lines = sourceFile.readlines()
    Transcripts = []
    for line in lines:
        attributes = line.split()
        Transcripts.append(Transcript(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4],attributes[5]))

    return Transcripts


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

def saveTranscripts(transcripts):
    sourceFile = open("transcriptions.txt", 'w')

    for transcript in transcripts:
        sourceFile.write(str(transcript.getDate()) + " " + str(transcript.getTime()) + " " +
        str(transcript.getAmount()) + " " + str(transcript.getEndingBalance()) + " " + transcript.getTransType() + " " + transcript.getEmail() + '\n')

run()