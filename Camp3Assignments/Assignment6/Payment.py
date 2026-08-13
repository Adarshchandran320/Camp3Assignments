from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def make_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount} using card ending in {self.card_number[-4:]}...")
        print("Payment Successful via Credit Card!\n")


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def make_payment(self, amount):
        print(f"Processing UPI payment of ${amount} for UPI ID: {self.upi_id}...")
        print("Payment Successful via UPI!\n")


class NetBankingPayment(Payment):
    def __init__(self, bank_name, user_id):
        self.bank_name = bank_name
        self.user_id = user_id

    def make_payment(self, amount):
        print(f"Processing Net Banking payment of ${amount} via {self.bank_name}...")
        print("Payment Successful via Net Banking!\n")




def process_order(payment_method: Payment, total_amount):
    print("Initiating Checkout...")
    payment_method.make_payment(total_amount)




card_opt = CreditCardPayment("4532-1234-5678-9876", "123")
upi_opt = UPIPayment("user@okaxis")
bank_opt = NetBankingPayment("HDFC Bank", "user_hdfc12")


process_order(card_opt, 150.00)
process_order(upi_opt, 45.50)
process_order(bank_opt, 500.00)