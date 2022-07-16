import os
currentdic =os.getcwd()
print(currentdic)
listfiles=os.listdir()
print(listfiles)
for a in range(len(listfiles)):
  print(listfiles[a])
os.chdir(r'C:\Users\ELCOT\Desktop\f1')
currentdicf1 =os.getcwd()
print(currentdicf1)
listfilesf1=os.listdir()
print(listfilesf1)
for a in range(len(listfilesf1)):
   print(listfilesf1[a])
os.chdir(r'C:\Users\ELCOT\Desktop\f2')
currentdicf2 =os.getcwd()
print(currentdicf2)
listfilesf2=os.listdir()
print(listfilesf2)
for a in range(len(listfilesf2)):
   print(listfilesf2[a])

print(f'first folder files:{listfilesf1}')
print(f'second folder files:{listfilesf2}')

s1=set(listfilesf1)
s2=set(listfilesf2)
print(s1.intersection(s2))
print(os.getcwd())
#os.mkdir('pythontraining')
#os.rename('pythontraining','abc')
#os.rename('4.txt','84.txt')

currentpath=os.getcwd()
years=[2020,2021]
print(currentpath)
for a in range(len(years)):
    os.chdir(r'C:\Users\ELCOT\Desktop\f2')
   # os.mkdir(str(years[a]))
    c=str(os.getcwd()+"\\"+str(years[a]))
    os.chdir(c)
    #for b in range(1,13):
        #os.mkdir(str(b))
import os.path
fileExit=os.path.isfile(r'C:\Users\ELCOT\Desktop\abc.txt')
print(fileExit)
if fileExit:
    print('file already present')
else :
    print('file not present in location')

import os.path
fileExit=os.path.isdir(r'C:\Users\ELCOT\Desktop\xyz')
print(fileExit)
if fileExit:
    print('folder already present')
else :
    #print('folder not present in location')
    print(os.path.dirname(r''))

#os.rmdir(r'C:\Users\ELCOT\Desktop\xyz')

print(os.getcwd())

for a in range(len(years)):
    os.chdir(r'C:\Users\ELCOT\Desktop\f2')
    m=str(os.getcwd()+"\\"+str(years[a]))
    os.chdir(m)
    f1=os.listdir()
    for b in range(len(f1)):
        os.rmdir(str(f1[b]))
        os.chdir(r'C:\Users\ELCOT\Desktop\f2')
        os.rmdir(str(years[a]))

