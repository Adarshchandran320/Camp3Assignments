from abc import ABC , abstractmethod

class foodorder(ABC):

    def placeorder(self):
        pass
        
    @abstractmethod
    def calaculate_bill(self):
        pass

class veg(foodorder):

    def placeorder(self):
        print("veg food order placed")

    def calaculate_bill(self,price,tax):
        total=price + tax
        print(f" veg price : {total}")

    
class nonveg(foodorder):

    def placeorder(self):
        print("non veg food orfer placed")

    def calaculate_bill(self,price,tax):
        total= price + tax
        print(f"nonveg price : {total}")


veg=veg()
nonveg=nonveg()

veg.placeorder()
veg.calaculate_bill(200,30)

nonveg.placeorder()
nonveg.calaculate_bill(500,35)