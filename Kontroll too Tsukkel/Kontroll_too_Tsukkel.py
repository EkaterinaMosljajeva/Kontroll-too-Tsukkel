from random import *
#5 variant

#1
try:
    dom=['  ~~~~~   ',
         ' /_____\  ',
         ' | []  |  ',
         '  -----   ']
    n=int(input("Majade arv(1-9): "))
    if n>0 and n<10:
        for k in dom:
            print(k * n)
    elif n>=10:
        print("Liiga suur!")
    elif n<=0:
        print("Liiga väike!")
except:
    print("Vale Andmetüüp")

#2
o=int(input("Sisesta õpilaste arv ühes klassis: "))
o=o*2
s=0
for x in range(1, o+1):
    h=randint(1,100)
    print(f"Õpilane {x}: {h}")
    s=s+h
s=s/o
print(f"Keskmine hinnang: {s}")

#5
try:
    min=int(input("Sisesta minimaalne väärtus: "))
    max=int(input("Sisesta maksimaalne väärtus: "))
    s=int(input("Sisesta samm: "))
    print("y=-0.5x+x")
    print()
    for x in range(min, max, s):
        y=-0.5*x+x
        print(f"x={x}\ny={y}")
        print()
except:
    print("Vale Andmetüüp")