#Devashish Kumar Yadav
#Code under MIT License

import re
import urllib2
from pprint import pprint

#import json
#data_file =  open('mini.json') 
#data = json.load(data_file)

# for student in data:
# 	if (student["h"]).find("HALL2") == 0 and student["r"]>=13000:
# 		print student["n"] + " " + type(student["r"])

data_file = open("y15.txt","w")

for i in range(150000, 150999):
	link = "http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt="+str(i)+"&sbm=Y"
	data_student = urllib2.urlopen(link).read()
	if data_student.find("HALL2") >=0:
		name = re.search(r"<b>Name: <\/b>([\n\ \	])([0-9a-zA-Z\ \	]*)",data_student)
		name_str = str(i)+" "+name.group(2).strip()+"\n"
		data_file.write(name_str)

data_file.close()

data_file = open("y14.txt","w")

for i in range(14000, 14999):
	link = "http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt="+str(i)+"&sbm=Y"
	data_student = urllib2.urlopen(link).read()
	if data_student.find("HALL2") >=0:
		name = re.search(r"<b>Name: <\/b>([\n\ \	])([0-9a-zA-Z\ \	]*)",data_student)
		name_str = str(i)+" "+name.group(2).strip()+"\n"
		data_file.write(name_str)

data_file.close()

data_file = open("y13.txt","w")

for i in range(13000, 13999):
	link = "http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt="+str(i)+"&sbm=Y"
	data_student = urllib2.urlopen(link).read()
	if data_student.find("HALL2") >=0:
		name = re.search(r"<b>Name: <\/b>([\n\ \	])([0-9a-zA-Z\ \	]*)",data_student)
		name_str = str(i)+" "+name.group(2).strip()+"\n"
		data_file.write(name_str)

data_file.close()