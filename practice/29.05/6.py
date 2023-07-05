import os
os.system("cls")
a,b=map(float,input("A va B ni qiymatni kiriting: ").split())
n=int(input("n ni qiymatini kiriting: "))
x=b-a
k=x/n
for x in range(1,n):
    a+=k
    print(f"{a:.2f}",end="  ")