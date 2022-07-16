'''
arr=[5,4,1,7,8,1]
for j in range(0,len(arr)):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
         arr[i],arr[i+1] = arr[i+1],arr[i]
      print(arr)

#output
[1, 4, 5, 7, 8]
'''

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[5,6,7],[8,9,10],[11,12,13]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    print(i)
    for k in range(len(b)):
        print(k)
        for j in range(len(b[0])):
            print(j)
            c[i][j]+=a[i][k]*b[k][j]
            print(c)
print("result matrix")
for r in c:
    print(r)

