class Account:
    Accounts_opened = 0
    min_amt = 0
    loan_interest = 0
    collatoral = ["property", "house", "car","jewelry"]
    msg = "Account created"
    #   BANKobj = Bank()

    def __init__(self, name, age, address, phNo, email, amt_deposited):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phNo = phNo
        self.__email = email
        self.amt_deposited = amt_deposited
        self.transaction_limit = 0
        self.loan = []
        self.loans_taken = len(self.loan)

        def app_validation(self)-> bool:
        valid = False
        if(self.age >= 18 and len(self.phNo) == 10 and self.amt_deposited >= __class__.min_amt):
            valid = True
            Accounts_opened +=1

        return valid
        
        if(app_validation()):
            print(msg)
        else:
            print("ACCOUNT REJECTED DUE TO WRONG DETAILS.")
        
        #   self.loan_amt_check = amt_deposited
        return 


    def transaction(self, receiver_acc_num, amt)-> tuple:
        _status = False
        if(len(receiver_acc_num)==10 and (self.amt_deposited - amt) >= 0 and self.transaction_limit > 0):
            self.amt_deposited -= amt
            self.transaction_limit-=1
            _status = True
        
        return (_status, self.amt_deposited)

    def Deposit(self, amt):
        self.amt_deposited += amt
        return self.amt_deposited

    def Loan(self, amt:float, collatoral_index: int,self.evaluation_asset:float, time_yr: int):
        
        valid = False
        msg = "LOAN REJECTED! \n"
    
        if(amt <= evaluation_asset  and collatoral_index in range(1,4) and time_yr > 0 and Bank.AMOUNT):
            valid = True
            msg = "LOAN GRANTED!\n"
            self.loan.append((len(loan)+1), amt, evaluation_asset, collatoral[collatoral_index], __class__.loan_interest, time_yr, msg)

        if valid:
            return self.loan[-1]

        else :
            return valid
    
    

    
class SavAcc(Account):

    min_amt = 3000
    loan_interest = 12


    def __init__(self, name, age, address, phNo, email, amt_deposited):
        super().__init__(name, age, address, phNo, email, amt_deposited)
        self.transaction_limit = 6

    
        
class CrntAcc(Account):
    
    min_amt = 50000
    loan_interest= 5

    def __init__(self, name, address, phNo, email, amt_deposited, org_age):
        super().__init__(name, age, address, phNo, email, amt_deposited)


class Bank:
    """Bank will only be able to give loan if and only if it has sufficient amt itself"""
    CUSTOMERS = {}
    AMOUNT = 100000

    def __init__(self, Name) -> None:
        self.Name = Name
        self.report = open("Bank_Report.txt", "x+")

        

    @staticmethod
    def loan_approval(amt) -> bool:
        if(amt=<(0.25*Bank.AMOUNT)):
            return True
        else:
            return False
    
    @staticmethod
    def open():
        

class Manager:
    """Manager has the power to open the bank and w/o manager consent it won't open
    and once it opened then 
    """

    def __init__(self, Name):
        self.Name = Name
    
    @staticmethod
    def open_Bank():
        return True

    def
