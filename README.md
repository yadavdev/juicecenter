JuiceCenter 1.0beta
===============
> By Devashish Kumar Yadav &
>   Gaurav ,IIT Kanpur

A python Gui app for carrying out student's juice+icecream transactions.

How To Use(Inside IIT Kanpur):

1. Install Python2.7 and the following modules:
	* MySQLdb (MySQL-python)
	* PyQT4
	* Openpyxl (for output to excel sheets)
	* Pyinstaller (for creating exe files for windows)
2. Build Database for your hall by changing the "HALL" in scrapfromweb.py in scrap_data folder.
3. Create database in mysql and then in python fill tables by editing createdb.py according to your needs(year and hall wise).

4. Either run studentpage.py for the program or create executables on different platforms using pyinstaller
	pyinstaller src/studentpage.py
	pyinstaller --noconsole src/studentpage.py (If no console output desired and only GUI application needed)

Licensed under MIT License.
