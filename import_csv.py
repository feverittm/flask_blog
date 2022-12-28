import csv
import sqlite3


try:

	# Import csv and extract data
	with open('team_checkin.csv', 'r') as fin:
		dr = csv.DictReader(fin)
		student_info = [(i['idnum'], i['last_name'], i['first_name'], i['email'], i['cell'], i['status'], i['utype']) for i in dr]
		print(student_info)

	# Connect to SQLite
	sqliteConnection = sqlite3.connect('database.db')
	cursor = sqliteConnection.cursor()

	# Create student table
	cursor.executemany(
		"insert into members (idnum, last_name, first_name, email, cell, status, utype) VALUES (?, ?, ?, ?, ?, ?, ?);", student_info)

	# Show student table
	cursor.execute('select * from members;')

	# View result
	result = cursor.fetchall()
	print(result)

	# Commit work and close connection
	sqliteConnection.commit()
	cursor.close()

except sqlite3.Error as error:
	print('Error occurred - ', error)

finally:
	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')

