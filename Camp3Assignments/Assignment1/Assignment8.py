class mobilerecharge:
    mobile_number = ""
    balance = ""

    def recharge(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Recharge successful")
            print("Current Balance:", self.balance)
        else:
            print("Invalid recharge amount")

    def use_balance(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Balance used successfully")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient balance")

    def display(self):
        print("Mobile Number:", self.mobile_number)
        print("Current Balance:", self.balance)

mobile1=mobilerecharge()
mobile1.mobile_number="1234567890"
mobile1.balance=100

print("-------------------------------")
mobile1.display()

mobile1.use_balance(50)
mobile1.display()

mobile1.recharge(200)
mobile1.display()
