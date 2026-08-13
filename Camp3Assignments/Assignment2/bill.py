class BillingSystem:
    def __init__(self,country_name,language,customer_id,billing_date,amount_outstanding):
        self.country_name=country_name
        self.language=language
        self.customer_id=customer_id
        self.billing_date=billing_date
        self.amount_outstanding=amount_outstanding

    def display_details(self):
        print("\n Billing Info")
        print(f"Country Name:  {self.country_name}")
        print(f"Language:      {self.language}")
        print(f"Customer ID:   {self.customer_id}")
        print(f"Billing date:  {self.billing_date}")
        print(f"Amount:        {self.amount_outstanding}")

us_customer = BillingSystem("United States", "English", "US1001", "2026-08-01", 150.75)
japan_customer = BillingSystem("Japan", "Japanese", "JP2004", "2026-08-02", 3400.00)

us_customer.display_details()
japan_customer.display_details()