from abc import ABC,abstractmethod
class car(ABC):
    def mile(self):
        pass
class shift(car):
    def mile(self):
        print('shift car')
class Hundai(car):
    def mile(self):
        print('shift car')
s=shift()
s.mile()
H=Hundai()
H.mile()

from abc import ABC
class shape(ABC):
   @abstractmethod
   def volume(self):
        pass
class circle(shape):
    def volume(self):
        print('pi r square')
class rectangel(shape):
    def volume(self):
        print('v*b')
c=circle()
c.volume()
r=rectangel()
r.volume()

from tkinter import *
root=Tk()
root.title('checkbutton')
root.geometry('600x400')
var=IntVar()
def sel():
    selection=(var.get())
    print(selection)
Radiobutton(root,text="option11",variable=var,value=1,command=sel).grid(row=0,column=0)
Radiobutton(root,text="option12",variable=var,value=2,command=sel).grid(row=0,column=1)
Radiobutton(root,text="option13",variable=var,value=3,command=sel).grid(row=0,column=2)
Radiobutton(root,text="option14",variable=var,value=4,command=sel).grid(row=0,column=3)
root.mainloop()