import os
os.system("cls")
a=float(input("a ni qiymatini kiriting: "))
n=int(input("n ni qiymatini kiriting: "))
for x in range(1,n+1):
    print(f"{a:g}^{x}={a**x:g}")
    