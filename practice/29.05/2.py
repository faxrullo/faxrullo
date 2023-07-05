import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
S=0
sch=1
x=1.1
while n>=sch:
    if sch%2:
        S+=x
    else:
        S-=x
    sch+=1
    x+=0.1
print(f"Reslut: {S:.1f}")