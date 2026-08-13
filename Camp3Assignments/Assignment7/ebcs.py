class ElectricityBill:
    def calculate_bill(self, units):
        Bill_amount = units * 5
        print(f"Bill Amount using a base rate of $5 per unit:{Bill_amount}")


class DomesticBill(ElectricityBill):
    def calculate_bill(self, units):
        if units <= 100:
            Bill_amount = units * 5
            print(f"Bill Amount:{Bill_amount}")
        else:
            Bill_amount = (100 * 5) + ((units - 100) * 3)
            print(f"Bill Amount:{Bill_amount}")


class CommercialBill(ElectricityBill):
    def calculate_bill(self, units):
        Bill_amount = units * 8
        tax = Bill_amount * 0.10
        total = Bill_amount + tax
        print(f"Bill Amount:{total}")


base = ElectricityBill()
domestic = DomesticBill()
commercial = CommercialBill()

units = 150
base.calculate_bill(units)
domestic.calculate_bill(units)
commercial.calculate_bill(units)