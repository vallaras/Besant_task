
import sqlite3
stu_id=int(input("enter the student id: "))
stu_name=str(input("enter the student name: "))
stu_m1=int(input("enter the student mark1: "))
stu_m2=int(input("enter the student mark2: "))
stu_m3=int(input("enter the student mark3: "))
total=stu_m1+stu_m2+stu_m3
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
conn=sqlite3.connect(r'C:\Users\ELCOT\student.db ')
cur=conn.cursor()
sql=f"insert into student values({stu_id},'{stu_name}',{stu_m1},{stu_m2},{stu_m3},'{total}','{avg}','{g}')"
print(sql)
cur.execute(sql)
conn.commit()



