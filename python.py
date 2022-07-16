import sqlite3
a=str(input("enter the emp name"))
b=str(input("enter the emp email id"))
c=str(input("enter the emp location"))
conn=sqlite3.connect("employee.db")
cur=conn.cursor()
s=f"insert into employees(name,email,address) values('{a}','{b}','{c}')"
print(s)
cur.execute(s)
cur.close()
conn.commit()
