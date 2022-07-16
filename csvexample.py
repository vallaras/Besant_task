import csv
import os
n1=int(input("enter the number1"))
n2=int(input("enter the number2"))
result=n1+n2
fileexit=os.path.isfile(r'C:\Users\ELCOT\Desktop\abc.csv')
print(fileexit)
if fileexit:
    print("file present")
    with open(r'C:\Users\ELCOT\Desktop\abc.csv','a')as file:
     write=csv.writer(file)
     write.writerow(['n1','n2','result'])
     write.writerow([n1,n2,result])
else:
    print("file not present")
    with open(r'C:\Users\ELCOT\Desktop\abc.csv','w')as file:
        write=csv.writerow(file)
        write.writerow(['n1','n2','result'])
        write.writerow([n1, n2, result])


with open(r'C:\Users\ELCOT\Desktop\abc123.csv','a')as file:
    write=csv.writer(file)
    write.writerow(['name','mark1'])
    write.writerow(['babu','8a'])

with open(r'C:\Users\ELCOT\Desktop\abc123.csv','r')as file:
    r=csv.reader(file)
    for a in r:
        print(a)




