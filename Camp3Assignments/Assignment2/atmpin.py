class Verify:
    y=1234
    def __init__(self,pin):
        if pin == Verify.y:
            print("Access granted")
        else:
            print("Denied")
user_input =int(input("Enter the ATM pin:"))
atm_check=Verify(user_input)
        
    