import os
os.system("cls")
a=float(input("a ni qiymatini kiriting: "))
n=int(input("n ni qiymatini kiriting: "))
s=0
for x in range(n+1):
    s+=(a**x)*(-1**x)
print(f"S={s:.2f}") 