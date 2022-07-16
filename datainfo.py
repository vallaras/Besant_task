import sqlite3

con = sqlite3.connect("product11.db")
print("Database opened successfully")

con.execute(
    "create table device (f1 text, f2 int, f3 int,f4 text)")

print("Table created successfully")

con.close()