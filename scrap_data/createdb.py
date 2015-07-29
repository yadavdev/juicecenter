#!/usr/bin/python

import MySQLdb

# Opening databse connection
# Preparing cursor object 
try:
	db = MySQLdb.connect("localhost","root","tiger","juicecenter")
	cursor = db.cursor()
except MySQLdb.Error, e:
	print "Database Connection Error"
	raise e


# Adding students to database

y13 = open("y13.txt")
y14 = open("y14.txt")
y15 = open("y15.txt")

cursor.execute("DROP TABLE IF EXISTS students")

createtable = """CREATE TABLE students (
				s_no INT(6),
				name CHAR(50),
				rollno INT(6),
				juice INT(6) default 0,
				icecream INT(6) default 0,
				total INT(6) default 0)"""

cursor.execute(createtable)


for i in range(190):
	data = y13.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	createtable = "CREATE TABLE "+'s'+str(rollno) + """(
													s_no INT(6) not null auto_increment primary key,
													date_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
													item CHAR(30),
													amount INT(6))"""

	cursor.execute(createtable)

	cursor.execute('insert into students (s_no ,name,rollno) values ("%d","%s", "%d")' % (i+1,name, rollno))
	#cursor.execute('insert into '+'s'+str(rollno) +(' (s_no ,name,rollno) values ("%d","%s", "%d")' % (i+1,name, rollno)))
	db.commit()

for i in range(200):
	data = y14.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	createtable = "CREATE TABLE "+'s'+str(rollno) +"""(
				s_no INT(6) not null auto_increment primary key,
				date_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
				item CHAR(30),
				amount INT(6))"""

	cursor.execute(createtable)

	cursor.execute('insert into students (s_no ,name,rollno) values ("%d","%s", "%d")' % (i+1+190,name, rollno))
	#cursor.execute('insert into '+'s'+str(rollno) +(' (s_no ,name,rollno) values ("%d","%s", "%d")' % (0,name, rollno)))
	db.commit()

for i in range(207):
	data = y15.readline()
	data = data.split()
	rollno = int(data[0])
	name = ' '.join(data[1:])
	createtable = "CREATE TABLE "+'s'+str(rollno) +"""(
				s_no INT(6) not null auto_increment primary key,
				date_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
				item CHAR(30),
				amount INT(6))"""

	cursor.execute(createtable)

	cursor.execute('insert into students (s_no ,name,rollno) values ("%d","%s", "%d")' % (i+1+290,name, rollno))
	#cursor.execute('insert into '+'s'+str(rollno)+(' (s_no ,name,rollno) values ("%d","%s", "%d")' % (0,name, rollno)))
	db.commit()

db.close()
y13.close()
y14.close()
y15.close()