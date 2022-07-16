import numpy as np
output=[]
str="my bike is mt and my bike color is black mt is an monster or torque"
print(str)
s=str.split(" ")
print(s)
v=np.array(s)
print(v)
uniq2, cnt2 = np.unique(v, return_counts = True)
print(uniq2)
print(cnt2)
for b in range(len(cnt2)):
    if cnt2[b]>1:
        output.append(uniq2[b])
print(output)


import numpy
print('Printing Original array')

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

print (sampleArray)

print('Array after deleting column 2 on axis 1')

sampleArray = numpy.delete(sampleArray , 1, axis = 0)

print (sampleArray)

arr = numpy.array([[10,10,10]])

print('Array after inserting column 2 on axis 1')

sampleArray = numpy.insert(sampleArray , 1, arr, axis = 0)

print (sampleArray)