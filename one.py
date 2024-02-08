import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password",
                               charset="utf8")

mycursor = mydb.cursor()

mycursor.execute("SHOW databases")
for x in mycursor:
    print(x)
  
mycursor.execute("USE shopdb")

mycursor.execute("SHOW Tables")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM product")
for x in mycursor:
    print(x)


name = 'Monitor 21"'
query = "SELECT * FROM product WHERE Name='" + name + "'"
mycursor.execute(query)
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

mycursor.close()
mydb.close()
