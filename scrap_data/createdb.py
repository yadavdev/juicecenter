#!/usr/bin/python

import MySQLdb

# Opening databse connection
db = MySQLdb.connect("localhost","root","","test")

# Preparing cursor object 
cursor = db.cursor()

# Adding students to database

y13 = open("y13.txt")
y14 = open("y14.txt")
y15 = open("y15.txt")

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS dues")

createtable = """CREATE TABLE students (
				name CHAR(50),
				rollno INT(6),
				img CHAR(15) )"""

cursor.execute(createtable)

createtable = """CREATE TABLE dues (
				name CHAR(50),
				rollno INT(6),
				img CHAR(15),
				due INT(10) default 0)"""

cursor.execute(createtable)

for i in range(190):
	data = y13.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	img = data[0] + "_0.jpg"
	cursor.execute('insert into students (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	cursor.execute('insert into dues (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	db.commit()

for i in range(200):
	data = y14.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	img = data[0] + "_0.jpg"
	cursor.execute('insert into students (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	cursor.execute('insert into dues (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	db.commit()

for i in range(207):
	data = y15.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	img = data[0] + "_0.jpg"
	cursor.execute('insert into students (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	cursor.execute('insert into dues (name,rollno,img) values ("%s", "%d", "%s")' % (name, rollno, img))
	db.commit()

db.close()
y13.close()
y14.close()
y15.close()