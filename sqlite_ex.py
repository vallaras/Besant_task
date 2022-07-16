import sqlite3
stu_id=int(input('enter the student id'))
stu_name=str(input('enter the student name'))
mark1=int(input('enter the mark1'))
mark2=int(input('enter the mark2'))
mark3=int(input('enter the mark3'))
total=mark1+mark2+mark3
avg=total/3
if avg>=90:
    g=('grade A')
elif avg>=70:
    g=('grade B')
elif avg>=50:
    g=('grade C')
elif avg<=35:
    g=('grade D')
else:
    g=('grade E')
conn=sqlite3.connect(r'C:\Users\ELCOT\PycharmProjects\trining\student10.db')
cur=conn.cursor()
sql=f"insert into test values({stu_id},'{stu_name}',{mark1},{mark2},{mark3},{avg},'{g}')"
print(sql)
cur.execute(sql)
conn.commit()