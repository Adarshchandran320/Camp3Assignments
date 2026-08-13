# Assignment 1: Product Inventory
# Create a class named Product to manage product details.
# Requirements
# Create a class with the following methods:
# • add_stock(quantity) – Add stock if quantity > 0.
# • sell(quantity) – Reduce stock if enough stock is
# available.
# • display() – Display product details.
# •
# Create an object and assign the following values manually:
# • product_name
# • price
# • stock_quantity

class Product:
    def __init__(self, product_name, price, stock_quantity):
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

    def add_stock(self, quantity):
        if quantity >0:
            self.stock_quantity += quantity
            print(f"Added {quantity} units to stock.")
        else:
            print("quantity must be greater than 0")

    def sell(self,quantity):
        if quantity > 0 and quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            print(f"Sold {quantity} units. Remaining stock: {self.stock_quantity}")
        else:
            print("Invalid quantity or insufficient stock.")

    def display(self):
        print(f"Product: {self.product_name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock Quantity: {self.stock_quantity}") 

objProduct1=Product("Laptop",999.99,10)
objProduct2=Product("Smartphone",499.99,20)
objProduct3=Product("Headphones",199.99,15)

objProduct1.display()
objProduct2.display()
objProduct3.display()