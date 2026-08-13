class OnlinePayment:
    def pay_online(self, amount):
        print(f"Online payment of ₹{amount} successful.")
        
class CashPayment:
    def pay_cash(self, amount):
        print(f"Cash payment of ₹{amount} received.")


class Billing(OnlinePayment, CashPayment):
    pass


bill = Billing()
bill.pay_online(1500)
bill.pay_cash(800)