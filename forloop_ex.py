count=1
z=65
for i in range(1,5):
    print(count,end="  ")
    print()
    for j in range(1,i+1):
        print(chr(z),end="  ")
    count+=1
    z+=1
    print()



for a in range(1,11):
    c=10
    for b in range(1,11):
        if c==a:
           print('x',end=" ")
           c-=1
        else:
            print(c,end=" ")
            c-=1
    print()

for a in range(1,5):
    if a%2==0:
        for b in range(1,a+1):
            print('even',end='  ')
        print()
    else:
        for b in range(1,a+1):
            print("*",end=' ')
        print()

for l in range(1,5):
    if l%1==0:
        for l in range(1,l+1):
            print('even',end=' ')
        print()
    else:
        for j in range(1,l+2):
         print()


c=1
for i in range(1,5):
    for j in range(1,i+1):
        if c%2==1:
            print(c,end=" ")
            c+=1
        else:
            print('even',end=" ")
            c+=1
    print()

import math
a=1245
b=25
i=a/b
print(math.ceil(i))

