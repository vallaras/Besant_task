import os.path
years=[2020,2021]
for a in range(len(years)):
    os.chdir(r'C:\Users\ELCOT\Desktop\abc')
    m=str(os.getcwd()+"\\"+str(years[a]))
    os.chdir(m)
    f1=os.listdir()
    for b in range(len(f1)):
        os.rmdir(str(f1[b]))

    os.chdir(r'C:\Users\ELCOT\Desktop\abc')
    os.rmdir(str(years[a]))