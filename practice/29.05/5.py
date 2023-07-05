import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
f=1
s=0
for x in range(1,n+1):
    f*=x
    s+=f
print(f"Result: {s}")