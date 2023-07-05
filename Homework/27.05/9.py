import os
os.system("cls")
n= int(input("n ni qiymatini kiriting: "))
k=int(input("1-sonni kiriting: "))
sch=0
for x in range(2,n+1):
    z=int(input(f"{x}-sonni kiriting: "))
    if(k>z):
        z=k
        sch+=1
        continue
    else:
        print(f"Buzgan son: {z}")
        break
if sch==n-1:
        print("True")  
        