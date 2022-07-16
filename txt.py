d={1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
b=list(d.keys())
x = int(input("Enter the stud_id:"))
if x in b:
    for key, value in d[x].items():
        print(key, ":", value)


def check(x):
    d = {1: {"name": "frathunan", "dept": "cse", "year": 4},
         2: {"name": "gopi", "dept": "b.com", "year": 3},
         3: {"name": "santhosh", "dept": "EEE", "year": 4}}
    b = list(d.keys())
    #x = int(input("Enter the stud_id:"))
    if x in b:
        for key, value in d[x].items():
            print(key, ":", value)
print(check(2))


def add():
    d = {1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
    b= list(max(d.keys()))
    count=0
    x = int(input("Enter the value:"))
    while count<=10:
        a = input("Enter the student Name:")
        b = input("Enter the student dept:")
        c = int(input("Enter the student year:"))
        count=count+1
        o = {count: {"Name": a, "dept": b, "year": c}}
        d.update(o)
        print(d)


add()

def add():
    d = {1:{"name":"frathunan","dept":"cse","year":4},
  2:{"name":"gopi","dept":"b.com","year":3},
  3:{"name":"santhosh","dept":"EEE","year":4}}
    v=list(d.keys())
    c=max(v)
    n = c + 1
    a = input("Enter the student Name:")
    b = input("Enter the student dept:")
    c = int(input("Enter the student year:"))
    w={n: {"Name": a, "dept": b, "year": c}}
    d.update(w)
    print(d)

add()



def check():
  d = {1: {"name": "frathunan", "dept": "cse", "year": 4},
       2: {"name": "gopi", "dept": "b.com", "year": 3},
       3: {"name": "santhosh", "dept": "EEE", "year": 4}}
  b = list(d.keys())
  x = int(input("Enter the stud_id:"))
  if x in b:
    for key, value in d[x].items():
      print(key, ":", value)

check()

def search():
  d = {1: {"name": "frathunan", "dept": "cse", "year": 4},
       2: {"name": "gopi", "dept": "b.com", "year": 3},
       3: {"name": "santhosh", "dept": "EEE", "year": 4}}
  b=list(d)
  x=int(input("Enter the student id:"))
  if x in b:
    print(d[x])
search()






