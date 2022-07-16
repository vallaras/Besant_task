import sqlite3

con = sqlite3.connect("web.db")
print("Database opened successfully")

con.execute(
    "create table long1 (UID INTEGER PRIMARY KEY AUTOINCREMENT, UNAME TEXT NOT NULL, CONTACT TEXT NOT NULL)")

print("Table created successfully")

con.close()