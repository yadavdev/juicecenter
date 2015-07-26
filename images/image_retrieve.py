#!/usr/bin/python

#author Devashish Kumar Yadav
# Code available under MIT License

import urllib
import MySQLdb

# Opening databse connection
db = MySQLdb.connect("localhost","root","","test")

# Preparing cursor object 
cursor = db.cursor()

cursor.execute("SELECT * FROM students")

all_data = cursor.fetchall()

for i in all_data:
	image_url = "http://oa.cc.iitk.ac.in:8181/Oa/Jsp/Photo/"+i[2]
	urllib.urlretrieve(image_url, i[2])

db.close()