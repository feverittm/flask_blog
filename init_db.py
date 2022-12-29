import sqlite3

connection = sqlite3.connect('database.db')


with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#cur.execute("INSERT INTO s (title, content) VALUES (?, ?)",
#            ('First ', 'Content for the first ')
#            )

#cur.execute("INSERT INTO s (title, content) VALUES (?, ?)",
#            ('Second ', 'Content for the second ')
#            )

connection.commit()
connection.close()
