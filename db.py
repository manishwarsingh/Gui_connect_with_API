import sqlite3

conn = sqlite3.connect('database1.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Foretees (id INTEGER PRIMARY KEY AUTOINCREMENT, day TEXT NOT NULL UNIQUE, stime text, person TEXT)')
print("Table created successfully")
conn.close()