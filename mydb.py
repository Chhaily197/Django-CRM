#Install Mdwl o you computer
# pip install mysql
#pip instal mysql-connector
#pip instal mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

#prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE django_db")

print("All Done!")

