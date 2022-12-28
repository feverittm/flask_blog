import csv
import sqlite3


try:

	# Import csv and extract data
	with open('team_checkin.csv', 'r') as fin:
		dr = csv.DictReader(fin)
		student_info = [(i['LAST NAME'], i['FIRST NAME']) for i in dr]
		print(student_info)

	# Connect to SQLite
	sqliteConnection = sqlite3.connect('database.db')
	cursor = sqliteConnection.cursor()

	# Create student table
	cursor.execute('drop table if exists team;')

	cursor.execute('create table team(lastname varchar2(10), firstname varchar2(10));')

	# Insert data into table
	cursor.executemany(
		"insert into team (lastname, firstname) VALUES (?, ?);", student_info)

	# Show student table
	cursor.execute('select * from student;')

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

