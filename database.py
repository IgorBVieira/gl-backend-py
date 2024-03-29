import mysql.connector
from mysql.connector import errorcode

try:
    conec = mysql.connector.connect(
        user="root", database="glearning", host="localhost", password=""
    )

    print("Connected to MySQL database")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

