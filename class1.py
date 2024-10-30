import mysql.connector
print("why")
connection = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="skitmashit",
    database="classicmodels",
)
if(connection.is_connected()):
    print("Yipeee!! DB is connectedo ")
else:
    print("DB culd not be connected")