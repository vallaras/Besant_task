import sqlite3
f1=input("Enter the product:")
f2=int(input("Enter the product value:"))
f3=int(input("Enter the version:"))
f4=input("Enter the Brand:")
conn=sqlite3.connect(r'C:\Users\ELCOT\PycharmProjects\trining\product3.db')
cur=conn.cursor()
sql=f"insert into device values('{f1}',{f2},{f3},'{f4}')"
print(sql)
cur.execute(sql)
conn.commit()