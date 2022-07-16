
import numpy as np
a=[1,2,3,4]
print(type(a))
print(a)
a1=np.array(a)
print(type(a1))
print(a1)
a2=[[1,2,3],[4,5,6],[7,8,9]]
print(type(a2))
print(a2)
a3=np.array(a2)
print(type(a3))
print(a3)
a4=[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]
print(type(a4))
print(a4)
a5=np.array(a4)
print(type(a5))
print(a5)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

# creating array from list
a = [1, 2, 3, 4, 5]
print(type(a))
arr = np.array(a)
print(type(arr))
print(arr)

#mixed element array
a = [2.5, 3.5, 7, 4.5, 8]
arr = np.array(a)
print(arr)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[9,12,13]]
print('List of List = ', a)
print(arr)
arr = np.array(a)
print(arr)

arr = np.random.randint(0, 5, size = 10)
print('Original Array = ', arr)
v=[1,2,3,4,5,6,7,8,9]
uniq = np.unique(v)
print('Unique Items in v = ', uniq)
v1 = np.random.randint(10, 100, size = (3, 5))
print('\n---Two Dimensional Random Original Array----\n', v1)
v2 = np.unique(v)
print('Unique Items in v = ', v2)
v = np.random.randint(0, 9, size = (2, 3, 8))
print('\n----Three Dimensional Random Original Array----\n', v)
uniq, cnt = np.unique(arr, return_counts = True)
print('Unique Items in arr = ', uniq)
print('Count Items in arr = ', cnt)

import numpy as np
rm1=[]
m1=[]
for a in range(1,4):
    m1=[]
    for b in range(1,4):
        n=int(input("enter the number1"))
        m1.append(n)
    rm1.append(m1)
    print()
print(rm1)
a1=np.array(rm1)
print(a1)
rm2=[]
m2=[]
for a in range(1,4):
    m2=[]
    for b in range(1,4):
        n=int(input("enter the number1"))
        m2.append(n)
    rm2.append(m2)
    print()
print(rm2)
a2=np.array(rm2)
print(a2)