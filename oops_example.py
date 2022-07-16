class employe  :
    pass
class training :
    print("inside class")
    course='phython'
o=training()
print(o.course)
print(training.course)
class tr :
    course='phython'
    def trainc(self) :
        cn=self.course
        print(f"we are study {self.course}")
o1=tr()
print(o1.course)
o1.trainc()

class student :
    stu_id=101
    st_name='babu'
    def __init__(self) :
        print("inside constr")
    def printmessage(self) :
        print(f"student_id={self.stu_id}and name={self.st_name}")
s=student()
s.printmessage()

class employe :
    emp_name="beena"
    emp_id=14
    emp_location="tambaram"
    emp_phn=9935678901

    def __init__(self) :
        print("emp")
    def printmessage(self) :
        print(f"emp_name={self.emp_name},id={self.emp_id},location={self.emp_location}and phn={self.emp_phn}")
e=employe()
e.printmessage()

class header:
    def __init__(self):
        print('______________')
        print("Welcome to Elect board of tamil nadu")
        print('___________')

class footer:
    def __init__(self):
        print('____________')
        print('plesas pay the bill on the time')
        print('____________')

class elecal:
    def cal(self,unitcon):
        units=unitcon
        if(units<=100):
            payAmount=units*1.5
            fixedcharge=25.00
        elif(units<=200):
            payAmount=(100*1.5)+(units-100)*2.5
            fixedcharge=75.00
        elif(units<=350):
            payAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
            fixedcharge=100.00
        else:
            payAmount=0
            fixedcharge=1500.00
        Total=payAmount+fixedcharge
        print("\nElectricity bill=%.2f"%Total)
units=int(input("please enter the number of units you consumed in a month"))
h=header()
cala=elecal()
cala.cal(units)
f=footer()

class employ:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print(f"ab={id},name={name},age={age}")
e=employ(1,'Babu',30)

class Employee:
    company='Tutorial class'
    def __init__(self,name,age,gender,course):
        self.name=name
        self.age=age
        self.gender=gender
        self.course=course
    def func_message(self):
        print('welcome to python programing')
        print(f'name={self.name}and age={self.age}and gender={self.gender}')
    def coursestude(self):
        print(f'{self.name}is studying{self.course}')
emp1=Employee('jack',25,'male','python')
print(emp1.company)
emp1.func_message()
emp1.coursestude()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp11=Employee('vallarasu',30,'male','python')
print(emp11.company)
emp11.func_message()
emp11.coursestude()
print(emp11.name)
print(emp11.age)
print(emp11.gender)









