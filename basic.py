lst = []
for j in range(0,3):
    a=int(input("enter the movie num:"))
    b=input("enter the movie name:")
    c=int(input("enter the year:"))
    d=input("enter the Actor:")
    lst.append([a, b, c, d])

print(lst)

[[1, 'beast', 2022, 'vijay'], [2, 'master', 2020, 'vijay'], [3, 'kaithi', 2019, 'karthi']]


a=[[1, 'beast', 2022, 'vijay'], [2, 'master', 2020, 'vijay'], [3, 'kaithi', 2019, 'karthi']]
x=int(input("enter the file Year:"))
for i in a:
    #print(i)
    if i==x:
        print(i)

class student :
    stu_id=100
    stu_name='valla'
    def __init__(self) :
        print("inside constr")
    def printmessage(self) :
        print(f"student_id={self.stu_id}and name={self.stu_name}")
s=student()
s.printmessage()

class student():
    stu_id=100
    stu_name='vallarasu'
    def __init__(self):
        print(" inside constr")
    def printmessage(self) :
        print(f"student_id={self.stu_id}and name={self.stu_name}")
s=student()
s.printmessage()