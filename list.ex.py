
L=list(range(0,101))
print(L)
for i in range(0,101,2):
    print('even number:',i)
for j in range(0,101,3):
    print('odd number:',j)


a=0
b=100
print('prime number and between lower and upper')
for num in range (a,b+1):
    if num >1:
        # Python program to display all the prime numbers within an interval

        a = 0
        b = 100

        print("Prime numbers between", a, "and", b, "are:")

        for num in range(a, b + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

