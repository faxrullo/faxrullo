import os
os.system("cls")
ls=list(map(int,input("List elementlarini kiriting: ").split()))
for x in ls:
    y=len(str(x))
    if (x//(10**(y-1)))%2==0:
        print(x,end=" ")