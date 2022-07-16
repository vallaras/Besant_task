'''
print(a)
a=5
b=10
print(a/b)
b=0
print(a/b)
'''
try:
    a=5
    print(a)
except:
    print('a is not defined')

finally:
    print('I will always run')

print("\n")

try:
    a=5
    b=0
    print(a/b)
except:
    print("b values is invalid")
finally:
    print("im run")

print("\n")

try:
    print('x')
except:
    print("an exception occurred")

try:
    print('x')
except:
    print("something went wrong")
finally:
    print("the 'try except'is finished")

try:
    print('x')
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")



try:
    c=((a+b)/(a-b))
except ZeroDivisionError:
    print("a/b result in 0")
else:
    print('c')



randomList=['a',0,2]
for entry in randomList:
    try:
        print("the entry is",entry)
        r=1/int(entry)
        break
    except Exception as e:
        print("Oops!",e.__class__,"occurred.")
        print("Next entry.")
        print()
        print("the reciprocal of",entry,"is",r)
    try:
        print("hello")
    except:
        print("something went wrong")
    else:
        print("Nothing went wrong")
