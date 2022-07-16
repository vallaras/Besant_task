
from tkinter import *
import csv
import os.path
root=Tk()
root.title('good')
root.geometry('800x400')
def sel():
    selection=(var.get())
    if selection==1:
        return 'male'
    else:
        return 'female'
def submitde():
    print('welcome to tkinter')
    fe=os.path.isfile(r'C:\Users\ELCOT\Desktop\xyz.csv')
    print(fe)
    if fe:
        with open (r'C:\Users\ELCOT\Desktop\xyz.csv','a')as file:
            w=csv.writer(file)
            a=n1.get()
            b=n2.get()
            r=a+b
            result=n3.set(a+b)
            gender=sel()
            w.writerow(['number1','number2','result'])
            w.writerow([a,b,r,gender])
    else:
        with open (r'C:\Users\ELCOT\Desktop\xyz.csv','a')as file:
            w=csv.writer(file)
            a=n1.get()
            b=n2.get()
            r=a+b
            result=n3.set(a+b)
            gender=sel()
            w.writerow(['number1','number2','result','gender'])
            w.writerow([a,b,r,gender])




Label(root,text="mark1").grid(row=0,column=0)
n1=IntVar()
Entry(root,textvariable=n1).grid(row=0,column=1)
n1.set('')
Label(root,text="mark2").grid(row=1,column=0)
n2=IntVar()
Entry(root,textvariable=n2).grid(row=1,column=1)
n2.set('')
Label(root,text="result").grid(row=2,column=0)
n3=IntVar()
Entry(root,textvariable=n3).grid(row=2,column=1)
n3.set('')
var=IntVar()
Label(root,text="Gender").grid(row=3,column=0)
Radiobutton(root,text="male",variable=var,value=1,command=sel).grid(row=3,column=1)
Radiobutton(root,text="female",variable=var,value=2,command=sel).grid(row=3,column=2)
Button(root,text='submit',command=submitde).grid(row=4,column=1)
root.mainloop()




from tkinter import *
root=Tk()
menu=Menu(root)
root.config(menu=Menu)
filemenu=Menu(menu)
menu.add.cascade(label='file',menu=filemenu)
filemenu.add.commend(label='new')
root.mainloop