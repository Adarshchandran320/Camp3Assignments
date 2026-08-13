class car:
    car_name=""
    fuel_capacity=0
    current_fuel=0

    def refill_fuel(self, litres):
        if litres > 0:
            self.current_fuel = self.current_fuel + litres
            print("fuel refilled")
            print("current fuel :", self.current_fuel)
        else:
            print("Cannot refill more than fuel capacity")

    def drive(self, litres):
        if litres <= self.current_fuel:
            self.current_fuel = self.current_fuel - litres
            print("Car driven successfully")
            print("Current Fuel :", self.current_fuel)
        else:
            print("Not enough fuel")

    def display(self):
        print("Car Name :", self.car_name)
        print("Fuel Capacity :", self.fuel_capacity)
        print("Current Fuel :", self.current_fuel)

car1=car()
car1.car_name="BMW"
car1.fuel_capacity=50
car1.current_fuel=20
car1.display()