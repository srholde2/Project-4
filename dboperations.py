
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="testuser1", passwd="Maxwasgreat16!")


cursor = db.cursor()
id = 1009
fname = 'Bob'
lname = 'Vance'
cname = 'Intro to Python'
clocation = 'B410'

cursor.execute("INSERT INTO BUS443.FACULTY(FIRSTNAME, LASTNAME, COURSENAME, COURSELOCATION) VALUES (%s,%s,%s,%s)",
               (fname,lname,cname,clocation))
cursor.execute("SELECT * FROM BUS443.FACULTY")

data = cursor.fetchall()

print(data)