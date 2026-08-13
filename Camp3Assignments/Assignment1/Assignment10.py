class ShoppingCart:

    item_name = ""
    item_price = 0
    quantity = 0

    def add_item(self, quantity):
        if quantity > 0:
            self.quantity = self.quantity + quantity
            print(quantity, "item added")
            print("Current Quantity :", self.quantity)
        else:
            print("Invalid Quantity")

    def remove_item(self, quantity):
        if quantity <= self.quantity:
            self.quantity = self.quantity - quantity
            print(quantity, "items removed")
            print("Remaining Quantity :", self.quantity)
        else:
            print("Cannot remove more items than available.")

    def display(self):
        print("Item Name :", self.item_name)
        print("Item Price :", self.item_price)
        print("Quantity :", self.quantity)

cart1 = ShoppingCart()
cart2 = ShoppingCart()
cart3 = ShoppingCart()

cart1.item_name = "Laptop"
cart1.item_price = 55000
cart1.quantity = 10

cart2.item_name = "Keyboard"
cart2.item_price = 1500
cart2.quantity = 20

cart3.item_name = "Mouse"
cart3.item_price = 800
cart3.quantity = 15


print("=====================")

cart1.display()
print()

cart2.display()
print()

cart3.display()


cart1.remove_item(4)
cart2.remove_item(5)
cart3.remove_item(3)

print("\n========== AFTER REMOVING ==========")

cart1.display()
print()

cart2.display()
print()

cart3.display()


cart1.add_item(2)
cart2.add_item(3)
cart3.add_item(5)

cart1.display()
print()

cart2.display()
print()
