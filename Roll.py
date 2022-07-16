x=int(input("Enter the Headvalue:"))
y=int(input("Enter the Legvalue:"))
if x<15:
    head=x//2
    print("chiken ",":",head)
    head=x//4
    print("Rabit ", ":", head)
    ck_head = y // 2
    print("Chiken Head:", ck_head)
    rb_head = y % 4
    print("Rabit Head:", rb_head)


else:
    print("Invalid value")







