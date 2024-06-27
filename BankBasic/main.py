import BankBasic as BB

def screen0():
    in1 = int(input("Welcome, \n1. Login \n2.Sign up\n\n\tSelect an option>   "))
    return in1

while(true):
    
    if screen0() == 0:
        print("\t\tLOGIN PAGE\n")
        
        custid = input("Enter CustID: ")
        pswrd  = input("Enter Password: ")

        