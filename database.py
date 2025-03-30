# Bank management system
# here we import a mysql as a database using mysql.connector
import mysql.connector as sql

# here we define our database host, user, password and database name
mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Vaibhav@2004",
    database="bank"
)

cursor = mydb.cursor()


def db_query(query_str, params=None):
    if params:
        cursor.execute(query_str, params)
    else:
        cursor.execute(query_str)
    result = cursor.fetchall()
    return result


# here we make a customer table
def create_customer_table():
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS Customers
          (username VARCHAR(50) NOT NULL,
          password VARCHAR(20) NOT NULL,
          name VARCHAR(50) NOT NULL,
          age INTEGER NOT NULL,
          city VARCHAR(20) NOT NULL,
          balance INTEGER NOT NULL,
          account_number INTEGER,
          status BOOLEAN)
     ''')


mydb.commit()
# here main() function started
if __name__ == "__main__":
    create_customer_table()
