from abc import ABC, abstractmethod

# 1. Abstract Base Class
class BankAccount(ABC):
    def __init__(self, account_no, holder_name, balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self._balance = float(balance)

    # Abstract method 1
    @abstractmethod
    def deposit(self, amount):
        pass

    # Abstract method 2
    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance


# 2. Savings Account (Rules: Must maintain a minimum balance of $500)
class SavingsAccount(BankAccount):
    MIN_BALANCE = 500.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"[Savings] Deposited ${amount}. New balance: {self._balance}")
        else:
            print("[Savings] Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("[Savings] Invalid withdrawal amount.")
        elif self._balance - amount < self.MIN_BALANCE:
            print(f"[Savings] Withdrawal denied! Must keep at least {self.MIN_BALANCE} minimum balance.")
        else:
            self._balance -= amount
            print(f"[Savings] Withdrew {amount}. Remaining balance: {self._balance}")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f" Deposited {amount}. New balance: {self._balance}")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif (self._balance - amount) < -self.OVERDRAFT_LIMIT:
            print(f" Withdrawal denied! Exceeds overdraft limit of ${self.OVERDRAFT_LIMIT}.")
        else:
            self._balance -= amount
            print(f" Withdrew {amount}. Remaining balance: {self._balance}")




print(" SAVINGS ACCOUNT ")
savings = SavingsAccount("SA101", "Ramu", balance=1000)
savings.deposit(200)       
savings.withdraw(500)      
savings.withdraw(300)      

print("\n  CURRENT ACCOUNT ")

current = CurrentAccount("CA202", "Priya", balance=500)
current.withdraw(1200)     
current.withdraw(500)      
current.deposit(1000)      