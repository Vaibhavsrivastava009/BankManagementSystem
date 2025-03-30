# bank services
from database import *
from register import *
from customer import *
import datetime


class Bank:

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number


    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                 f"(timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")

    def balance_enquiry(self):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = %s;", (self.__username,))
        print(f"{self.__username} Balance is {temp[0][0]}")


    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = %s;", (self.__username,))
        test = amount + temp[0][0]
        db_query(f"UPDATE Customers SET balance = '{test}' WHERE username = %s;", (self.__username,))
        self.balance_enquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Successfully Deposited into your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = %s;", (self.__username,))
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
            db_query(f"UPDATE Customers SET balance = '{test}' WHERE username = %s;", (self.__username,))
            self.balance_enquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            print(f"{self.__username} Amount is Successfully Withdraw From your Account {self.__account_number}")


    def fundtransfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM Customers WHERE username = %s;", (self.__username,))
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(f"SELECT balance FROM Customers WHERE account_number = %s;", (receive,))
            if not temp2:
                print("Account Number Does not Exists")
            else:
                test1 = temp[0][0] - amount
                test2 = amount + temp2[0][0]
                db_query(f"UPDATE Customers SET balance = '{test1}' WHERE username = %s;", (self.__username,))
                db_query(f"UPDATE Customers SET balance = '{test2}' WHERE account_number = %s;", (receive,))
                receiver_username = db_query(f"SELECT username FROM Customers WHERE account_number = %s;", (receive,))
                self.balance_enquiry()
                db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer From {self.__account_number}',"
                         f"'{amount}'"
                         f")")
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer -> {receive}',"
                         f"'{amount}'"
                         f")")
            print(f"{self.__username} Amount is Successfully Transfer From your Account {self.__account_number}")

