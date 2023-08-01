# install mysql on my computer
# pip install mysql
# pip install mysql-connector-python

# login to the admin
# username : jobekis, mdp : dcrm23


import mysql.connector

dataBase = mysql.connector.connect(
	host 	= 'localhost',
	user 	= 'root',
	passwd 	= '',
	)

# prepare a curor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE db_dcrm")

print("All done!")
