import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
a=False
for x in range(2,n):
    son=x
    for y in range(2,int(x**(1/2))+1):
        a=False
        while x>=0:
            x-=y
            if x==0:
                a=True
                break
        if a:
            break
    if a==False:
        print(son,end=" ")