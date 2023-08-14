import sqlite3

#   Establish a connection and a cursor
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE band='Monkey'")
cursor.execute("SELECT * FROM events WHERE date='31.10.2091'")
cursor.execute("SELECT * FROM events")  # Query all data
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE band='Monkey'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
events = [('Cats', 'Yozgat', '31.10.2091'), ('Dogs', 'Sivas', '4.3.2093')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", events)
cursor.execute("SELECT * FROM events")
# conn.commit()
rows = cursor.fetchall()
print(rows)