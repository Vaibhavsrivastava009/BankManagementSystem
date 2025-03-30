from database import *


class Customer:
    def __init__(self, username, password, name, age, city, account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createUser(self):
        # Use a parameterized query for safety
        query = '''
            INSERT INTO Customers (username, password, name, age, city, balance, account_number, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self.__username, self.__password, self.__name, self.__age, self.__city, 0, self.__account_number, True)

        cursor.execute(query, params)
        mydb.commit()
        print("Customer created successfully!")
