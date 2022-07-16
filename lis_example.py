list=[[1,2,3,4],[4,5,6,7],[8,9,10,11]]
print(list)
print(list[1][1])
print(list[0][3])
for i in list:
    print(i)

a = [[1,2,3],'a', 'b',  [4,5,6], 'd', [7,8,9]]
b = []
for i in a:
    b.extend(i)
print(b)


a = [[1,2,3], [4,5,6], [7,8,9]]
z=0
for i in range(0,3):
    x=a[i][i]
    z+=x
print(z)








#o/p : [1,2,3,4,5,6,7,8,9]