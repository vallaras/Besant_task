def fun():
    str="National highway"
    x="nh4"
    return[str,x]
list=fun()
print(list)

def sum(number):
    total=0
    for i in number:
        total+=i
    return total
print(sum((8,2)))

def number(multi):
    total=1
    for i in multi:
        total*=i
    return total
list=number((8,2,3,-1,7))
print(list)


def enumber(a):
    l=[]
    for i in a:
        if i%2==0:
            l.append(i)
    return l
print(enumber([1,2,3,4,5,6,7,8,9]))

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')


