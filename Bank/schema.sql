schema

Accounts    
    {
        id pri unique
        name
        add
        phone 
        emial
        age
        geneder Char (1)
        amt
        fd default: Null
        rd default: Null
        interest_on_savingss
        date of acc opening DATE
        last_updated DATE
        // locker facility Null;
        Transactions done //imposes limit for savings acc

    }

    Transactions
    {
        id foreign 
        amt
        date
        status success/failure
        message in case of failure, default: None
        time
        to?
        Transactionsid 


    }

    Bank Report {
        Accounts opened
        date
        cash_in
        cash_out
        total
        // at the premesis kinda complex can be ignored;

    }
^^^ has to be updated at the end of the day therefore the c_in and c_out can happen at the script hand and the updated in the db

CREATE TABLE[IF NOT EXISTS] Accounts(
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
