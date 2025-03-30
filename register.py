# User Registration Signin() or Signup()
import random
from customer import *
from bank import Bank


def signUp():
    while True:
        username = input("Create Your Username: ")

        # Use parameterized query to prevent SQL injection
        temp = db_query(f"SELECT username FROM Customers WHERE username = %s;", (username,))
        if temp:
            print("Username already exists, please choose another one.")
        else:
            print("Username is available, please proceed...")
            break

    password = input("Enter Your Password: ")  # Keeping password as a string for complexity
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    city = input("Enter Your City: ")

    # Generating a unique account number
    while True:
        account_number = random.randint(100000000, 999999999)  # 9 digits random number
        temp = db_query(f"SELECT account_number FROM Customers WHERE account_number = %s;", (account_number,))
        if temp:
            continue  # If account number exists, generate again
        else:
            print(f"Your Account Number is: {account_number}")
            break

    # Creating Customer object
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createUser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()


def signIn():
    username = input("Enter your username: ")
    temp = db_query(f"SELECT username FROM Customers WHERE username = %s;", (username,))
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} enter your password: ")
            temp = db_query(f"SELECT password FROM Customers WHERE username = %s;", (username,))
            if temp[0][0] == password:
                print("SignIn Successfully....")
                return username
            else:
                print("Wrong password try again...")

    else:
        print("Enter correct username.... ")
        signIn()
