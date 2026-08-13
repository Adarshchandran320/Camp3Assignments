# Assignment 3: Bank Account
# Create a class named BankAccount.
# Requirements
# Methods:
# • deposit(amount)
# • withdraw(amount)
# • display()
# Rules
# • Deposit amount must be greater than 0.
# • Withdraw amount must not exceed balance.
#  Create an object and manually assign:
# • account_holder
# • account_number
# • balance
class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print("Successfully deposited")
        else:
            print("Deposit amount must be greater than 0")
    def withdraw(self,amount):
        if amount<=0:
            print("withdraw amount must be greater than 0")
        elif amount<= self.balance:
            self.balance -=amount
            print("withdraw amount must be lower than the avilable balance")
        else:
            print("Insufficient balance!")
    def display(self):
        print(f"Holder Name:{self.account_holder}")
        print(f"Account number:{self.account_number}")
        print(f"Balance:{self.balance}")
objBankAccount1=BankAccount("Alwin",2546454845,8000.00)
objBankAccount1.display()