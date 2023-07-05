import os
os.system("cls")
n=int (input("n ni qiymatini kiriting: "))
for x in range(1,n):
    if x**(1/2)==int(x**(1/2)):
        for y in range(1,int(x**(1/2))):
            for z in range(y,int(x**(1/2))):
                if((y**2+z**2)==x):
                    print(x,end=" ")