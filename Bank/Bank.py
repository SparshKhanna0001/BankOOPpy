import sqlite3 as sql

"""Database inilisation process"""

con = sql.connect("bank.db")
cur = con.cursor()
cur.execute('''CREATE TABLE[IF NOT EXISTS] Accounts(
    CustId Char(10) PRIMARY KEY,
    Name Varchar(100) NOT NULL,
    Age INT(3) NOT NULL,
    MNo INT(10) NOT NULL unique,
    email Varchar(100) unique NOT NULL,
    Address Varchar(300) NOT Null,
    acc_opened DATE,
    last_updated DATE,
    FD INT default=0, 
    locker_no INT(2) ,
    Transactions done INT(5) default=0,
    amt FLOAT(24),
    Loan default=0 INT(1),
    Type default="sav" CHAR(3),
);

CREATE TABLE[IF NOT EXISTS] Transactions(
    CustId CHAR(10) PRIMARY KEY,
    Amt FLOAT(24) NOT NULL,
    Status CHAR(7) NOT NULL,
    Date DATE,
    Time TIME,
    Receiver CHAR(10),
    TransactionID INT(15),
    FOREIGN KEY (CustId) REFERENCES Accounts(CustId)
);

CREATE TABLE[IF NOT EXISTS] Report( 
    Date DATE PRIMARY KEY,
    Status Char(4) default="clos",
    Cash_in FLOAT(24),
    Cash_out Float(24),
    Total FLOAT(24), 
)

CREATE TRIGGER Report
AFTER INSERT OR UPDATE OF Cash_in, Cash_out ON Report
BEGIN 
    UPDATE Report
    SET Total = Cash_in - Cash_out;
    WHERE Date = NEW.Date
END
''')

""" Defining the basic structure of the class; Account"""
class Account:
    Accounts_opened = 0

    def __init__(self, name, age, address, phNo, email, amt_deposited):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phNo = phNo
        self.__email = email

    
    def id_gen(self)-> str:
        pass

    def app_validation(self)-> bool:
        pass

    def db_upload(self) ->bool:
        pass

    def transaction(self, receiver_acc_num, amt):
        pass

    
class SavAcc(Account):

    def __init__(self, name, age, address, phNo, email, amt_deposited):
        super().__init__(name, age, address, phNo, email, amt_deposited)

    def id_gen(self):
        try:
            cur.execute('''SELECT  C''')



