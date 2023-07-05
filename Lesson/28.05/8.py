import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
f1=1
f2=1
for x in range (1,n):
    f=f1+f2
    f1=f2
    f2=f
    print(f)