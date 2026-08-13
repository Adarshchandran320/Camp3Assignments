class Account:
    def Account_details(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
class SavingsAccount(Account):
    def cal(self,rate):
        interest=self.balance*rate/100
        print("Account Details")
        print(f"Account No: {self.account_no}")
        print(f"Balance:{self.balance}")
        print(f"Interest:{interest}")

obj1=SavingsAccount()
obj1.Account_details(1234,500)
obj1.cal(5)