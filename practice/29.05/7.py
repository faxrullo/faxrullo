import os
os.system("cls")
n=int(input("n ni qiymatini kiriting: "))
s=0
for x in range(1,n+1):
    s+=x**(n+1-x)
print(f"result: {s}")