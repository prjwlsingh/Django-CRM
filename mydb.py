import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'qwerty'

    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a dataBase
cursorObject.execute("CREATE DATABASE mw2")

print("ALL Done!")
