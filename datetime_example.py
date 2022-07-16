import datetime
dt=datetime.date.today()
dt1=datetime.datetime.now()
print(dt)
print(dt1)
print(f"yearvalue={dt1.year}")
print(f"dayvalue={dt1.day}")
print(f"Hourvalue={dt1.hour}")
print(f"minutevalue={dt1.minute}")
print(f"secondvalue={dt1.second}")
print(f"max year in year={datetime.MAXYEAR}")
print(f"min year in abc={datetime.MINYEAR}")
print(dt1.date())
print(dt1.time())
dt3=datetime.date(2022,1,2)
print(dt3)
dt4=datetime.datetime(2022,1,31,7,12,13)
print(dt4)
y=int(input('enter the year'))
m=int(input('enter the month'))
d=int(input('enter the day'))
h=int(input('enter the hour'))
mm=int(input('enter the minute'))
s=int(input('enter the second'))
dt5=datetime.datetime(y,m,d,h,mm,s)
print(dt5)
hour_replace=dt5.replace(hour=2)
print(hour_replace)

import datetime
dt=datetime.date.today()
dt1=datetime.datetime.now()
print(dt)
print(dt1)
print(f"year value={dt1.year}")
yearofbirth=int(input('enter the year of birth'))
age=(dt1.year)-yearofbirth
print(age)





