from register import *
from customer import *
from bank import *

status = False
print("Welcome to Vaibhav's Bank Management System...")

while True:
    try:
        choice = int(input("1. SignUp: \n"
                           "2. SignIn: "))
        if choice == 1:
            signUp()
        elif choice == 2:
            user = signIn()
            status = True
            break
        else:
            print("Please enter a valid input from options....")
    except ValueError:
        print("Invalid input, try again with numbers...")

account_number = db_query("SELECT account_number FROM customers WHERE username = %s;", (user,))

print(f"Welcome {user.capitalize()} Choose your Banking Service\n")
while status:
    try:
        facility = int(input("1. Balance Enquiry: \n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"
                             "5. Exit\n"))
        if 1 <= facility <= 5:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balance_enquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver account number: "))
                        amount = int(input("Enter Money to transfer: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 5:
                print("Thanks For Using Banking Services")
                status = False
        else:
            print("Please Enter Valid Input From Options...")
            continue
    except ValueError:
        print("Invalid Input Try again with Numbers...")
        continue
