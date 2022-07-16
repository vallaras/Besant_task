class classmethodexample:
    def withoutclassmethod(self):
        print("withoutclassmethod")
    @classmethod
    def withclassmethod(self):
        print("insideclassmethod")
classmethodexample.withclassmethod()
classmethodexample.withclassmethod()
classmethodexample.withoutclassmethod=classmethod(classmethodexample.withoutclassmethod)
classmethodexample.withoutclassmethod()
class student:
    @classmethod
    def printmessage(self):
        id=int(input("enter the number"))
        name=int(input("enter the name"))
        m1=int(input("enter the mark1"))
        m2 = int(input("enter the mark2"))
        m3 = int(input("enter the mark3"))
        total=m1+m2+m3
        if total>=280:
            g='A'
        elif total<280 and total>=250:
            g='B'
        else:
            g='C'
        print(f"{name} and its id ={id} and he scored {total} secured {g} grade in exam ")
student.printmessage()

class classmethodexample:
    def withoutclassmethod(self):
        print("withoutclassmethod")
    @classmethod
    def withclassmethod(cls):
        print("insideclassmethod")
        cls.staticmethodexample()
    @staticmethod
    def staticmethodexample():
        print("welcome")
        print("________")
classmethodexample.withclassmethod()


class A:
    def __init__(self):
        print("prent clss constructor")
    def parantclass(self):
        print("welcome to python parent class")
        print("______")
class B(A):
    def __init__(self):
        A.__init__(self)
        A.parantclass(self)
        print("child class constructor")

    def childclass(self):
        print("Welcome to python child class 2.0")
        print("________")
childobj=B()
childobj.childclass()

class grandfather:
    def __init__(self):
        print("welcome to school")
    def childclass(self):
        print("ARM College")
class father(grandfather):
    def __init__(self):
        grandfather.__init__(self)
        grandfather.childclass(self)
        print("best of luck")
    def classmate(self):
        print("wel come to fatherclass")


class child(father):
    def __init__(self):
        father.__init__(self)
        father.classmate(self)
        print('welcome')
    def mother(self):
        print("cool")
childobj=child()
childobj.mother

class father:
    def __init__(self):
        print('good morning')
    def AA(self):
        print('welcome')
class mother:
    def __init__(self):
        print('flight')
    def bb(self):
        print('valla')
class child(father,mother):
    def __init__(self):
        father.__init__(self)
        father.AA(self)
        mother.__init__(self)
        mother.bb(self)
        print('college')
    def CC(self):
        print('vibe')
childobj=child()
childobj.CC()
class school:
    def __init__(self):
        print('techer')
    def AA(self):
        print('project')
class student1(school):
    def __init__(self):
        school.__init__(self)
        print('download')
    def BB(self):
        print('bookmark')
class student2(school):
    def __init__(self):
        school.__init__(self)
        print('mango')
    def CC(self):
         print('orenge')
class student3(school):
    def __init__(self):
        school.__init__(self)
        print('good')
    def DD(self):
         print('bad')
childobj=student3()
childobj.DD()
childobj=student2()
childobj.CC()
childobj=student1()
childobj.BB()
childobj=school()
childobj.AA()

class grandfather:
    def __init__(self):
        print('bookback')
    def XY(self):
        print('notepad')
class father(grandfather):
    def __init__(self):
        grandfather.__init__(self)
        grandfather.XY(self)
        print('cool')
    def XZ(self):
        print('laptop')
class mother:
    def __init__(self):
        print('vallarasu')
    def XQ(self):
        print('search')
class child(father,mother):
    def __init__(self):
        father.__init__(self)
        father.XZ(self)
        mother.__init__(self)
        mother.XQ(self)
        print('frathunan')
    def XA(self):
        print('moon')
childobj=child()
childobj.XA()

class emp:
    def __init__(self,name,id,age,location):
        self.id=id
        self.name=name
        self.age=age
        self.location=location
    def parentprint(self):
        print(f'the emp_id={self.id}and name={self.name} and age={self.age}and location={self.location} ')
class dept(emp):
    pass
o=dept('vallarasu',1,21,'chennai')
o.parentprint()

class emp1:
    def __init__(self,name,id,age,location):
        self.id=id
        self.name=name
        self.age=age
        self.location=location
    def printmessage(self):
        print(f"The emp.id={self.id} , name={self.name} , age={self.age} and location={self.location}")
class dept1(emp1):
    def __init__(self,name,id,age,location,department_id):
        emp1.__init__(self,name,id,age,location)
        emp1.printmessage(self)
        self.department_id=department_id
    def printchildmessage(self):
        print(f" the employee {self.name} was working on {self.department_id}  department")

o=dept1('vallarasu',4022,21,'RubyLandmark','Mech')
o.printchildmessage()

class grandfather:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printmessage(self):
        print(f"the grandfather.name={self.name},age={self.age}")
    def AA(self):
         print('parent')
class grandmother:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printmessage(self):
        print(f"the grandmother.name={self.name},age={self.age}")
    def BB(self):
        print('child')
class father(grandfather,grandmother):
    def __init__(self):
        grandfather.__init__(self)
        grandfather.AA(self)
        grandmother.__init__(self)
        grandmother.BB(self)
        print('relative')
    def CC(self):
        print('family')
class child(father):
    def __init__(self,name,age):
        father.__init__(self,name,age)
        father.printmessage(self)
    def printchildmessage(self):
        print(f" the employee {self.name}and age {self.age}")
    c=child('ram,57')
    c.printmessage
    def DD(self):
        print('welcome')




childobj=child()
childobj.DD()




