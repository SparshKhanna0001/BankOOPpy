import sqlite3 as sql

"""Database inilisation pr
ocess"""

con = sql.connect("bank.db")
cur = con.cursor()
# Combined SQL statements for creating tables and corrected trigger in SQLite

sql_commands = '''
-- Create Accounts table
CREATE TABLE IF NOT EXISTS Accounts (
    CustId CHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INTEGER NOT NULL,
    MNo INTEGER NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE NOT NULL,
    Address VARCHAR(300) NOT NULL,
    acc_opened DATE,
    last_updated DATE,
    FD INTEGER DEFAULT 0, 
    locker_no INTEGER,
    Transactions_done INTEGER DEFAULT 0,
    amt FLOAT(24),
    Loan INTEGER DEFAULT 0,
    Type CHAR(3) DEFAULT 'sav'
);

-- Create Transactions table
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustId CHAR(10) NOT NULL,
    Amt FLOAT(24) NOT NULL,
    Status CHAR(7) NOT NULL,
    Date DATE,
    Time TIME,
    Receiver CHAR(10),
    FOREIGN KEY (CustId) REFERENCES Accounts(CustId)
);

-- Create Report table
CREATE TABLE IF NOT EXISTS Report (
    Date DATE PRIMARY KEY,
    Status CHAR(4) DEFAULT 'clos',
    Cash_in FLOAT(24),
    Cash_out FLOAT(24),
    Total FLOAT(24)
);

-- Create or replace trigger Update_Report_Total
CREATE TRIGGER IF NOT EXISTS Update_Report_Total
AFTER INSERT ON Report
BEGIN 
    UPDATE Report
    SET Total = NEW.Cash_in - NEW.Cash_out
    WHERE Date = NEW.Date;
END;

CREATE TRIGGER IF NOT EXISTS Update_Report_Total_Update
AFTER UPDATE OF Cash_in, Cash_out ON Report
BEGIN 
    UPDATE Report
    SET Total = NEW.Cash_in - NEW.Cash_out
    WHERE Date = NEW.Date;
END;
'''

# Execute the SQL commands
cur.executescript(sql_commands)


con.close()